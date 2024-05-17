# Используем базовый образ Python
FROM python:3.9

# Устанавливаем зависимости для torchaudio
RUN apt-get update && apt-get install -y ffmpeg

# Устанавливаем необходимые библиотеки
RUN pip install transformers torch torchaudio

# Копируем текущую директорию в контейнер
WORKDIR /aiservice
COPY . /aiservice

# Устанавливаем модель и процессор
RUN python -c "from transformers import WhisperProcessor, WhisperForConditionalGeneration; model_id = 'openai/whisper-small'; WhisperProcessor.from_pretrained(model_id).save_pretrained('/app'); WhisperForConditionalGeneration.from_pretrained(model_id).save_pretrained('/app')"

RUN python -c "from transformers import GPT2Tokenizer, GPT2LMHeadModel; GPT2Tokenizer.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2').save_pretrained('/app'); GPT2LMHeadModel.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2').save_pretrained('/app')"

# Указываем команду для запуска скрипта
CMD ["python3", "main.py"]
