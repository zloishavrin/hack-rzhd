# Используем базовый образ Python
FROM python:3.9

# Устанавливаем зависимости для torchaudio
RUN apt-get update && apt-get install -y ffmpeg

RUN pip install transformers torch torchaudio fastapi uvicorn typing pydantic

WORKDIR /aiservice
COPY . /aiservice

# Устанавливаем модель и процессор
RUN python3 -c "from transformers import WhisperProcessor, WhisperForConditionalGeneration; model_id = 'openai/whisper-small'; WhisperProcessor.from_pretrained(model_id).save_pretrained('/app'); WhisperForConditionalGeneration.from_pretrained(model_id).save_pretrained('/app')"
RUN python3 -c "from transformers import GPT2Tokenizer, GPT2LMHeadModel; GPT2Tokenizer.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2').save_pretrained('/app'); GPT2LMHeadModel.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2').save_pretrained('/app')"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]