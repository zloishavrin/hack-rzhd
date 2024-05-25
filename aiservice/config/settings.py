import torch

class Settings:
    WHISPER_MODEL_ID = "openai/whisper-small"
    GPT2_MODEL_ID = "sberbank-ai/rugpt3small_based_on_gpt2"
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

settings = Settings()