import torchaudio
import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# Загрузка модели и процессора
model_id = "openai/whisper-small"
processor = WhisperProcessor.from_pretrained(model_id)
model = WhisperForConditionalGeneration.from_pretrained(model_id)

# Проверка доступности GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

def load_audio(file_path):
    waveform, sample_rate = torchaudio.load(file_path)
    resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
    return resampler(waveform)

def transcribe(file_path):
    audio = load_audio(file_path)
    inputs = processor(audio.squeeze().numpy(), return_tensors="pt", sampling_rate=16000)

    with torch.no_grad():
        predicted_ids = model.generate(inputs.input_features.to(device))
        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    
    return transcription
