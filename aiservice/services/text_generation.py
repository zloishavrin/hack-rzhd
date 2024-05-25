import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Загрузка токенайзера и модели GPT-2
tokenizer = GPT2Tokenizer.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2")
gpt2_model = GPT2LMHeadModel.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2")
gpt2_model.eval()  # Переводим модель в режим оценки (не тренировки)

# Проверка использования GPU, если доступен
device = "cuda" if torch.cuda.is_available() else "cpu"
gpt2_model.to(device)

def generate_text(prompt, max_length=100, num_beams=5, temperature=0.1):
    # Определяем допустимую длину для генерации с учетом длины промпта
    #max_prompt_length = gpt2_model.config.max_position_embeddings - max_length
    encoded_prompt = tokenizer.encode(prompt, return_tensors="pt").to(device)

    #if encoded_prompt.shape[-1] > max_prompt_length:
        #raise ValueError(f"Промпт слишком длинный. Допустимая длина промпта: {max_prompt_length} токенов.")

    # Генерируем текст
    output = gpt2_model.generate(
        encoded_prompt,
        max_length=encoded_prompt.shape[-1] + max_length,
        num_beams=num_beams,
        temperature=temperature,
        early_stopping=True,
        pad_token_id=tokenizer.eos_token_id,
    )

    # Декодируем и возвращаем сгенерированный текст
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text