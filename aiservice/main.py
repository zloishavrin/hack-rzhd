from transformers import WhisperProcessor, WhisperForConditionalGeneration, GPT2Tokenizer, GPT2LMHeadModel
import torchaudio
import torch

# Загрузка модели и процессора
model_id = "openai/whisper-small"
processor = WhisperProcessor.from_pretrained(model_id)
model = WhisperForConditionalGeneration.from_pretrained(model_id)

# Проверка доступности GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Функция для загрузки и обработки аудио файла
def load_audio(file_path):
    waveform, sample_rate = torchaudio.load(file_path)
    resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
    return resampler(waveform)

# Функция для предсказания текста из аудио
def transcribe(file_path):
    audio = load_audio(file_path)
    inputs = processor(audio.squeeze().numpy(), return_tensors="pt", sampling_rate=16000)

    with torch.no_grad():
        predicted_ids = model.generate(inputs.input_features.to(device))
        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    
    return transcription

# Загрузка токенайзера и модели GPT-2
tokenizer = GPT2Tokenizer.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2")
gpt2_model = GPT2LMHeadModel.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2")
gpt2_model.eval()  # Переводим модель в режим оценки (не тренировки)

# Проверка использования GPU, если доступен
gpt2_model.to(device)

def generate_text(prompt, max_length=50):
    # Кодируем начальное сообщение
    inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)

    # Генерируем текст
    output = gpt2_model.generate(inputs, max_length=max_length, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

    # Декодируем и возвращаем сгенерированный текст
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

if __name__ == "__main__":
    file_path = "test.mp3"
    transcription = transcribe(file_path)
    print("Transcription:", transcription)

    prompt = "Ваше начальное сообщение"
    generated_text = generate_text(prompt)
    print("Generated Text:", generated_text)
