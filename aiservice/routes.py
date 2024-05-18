from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import List
from services.audio_processing import transcribe
from services.text_generation import generate_text

router = APIRouter()

@router.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...), strings: List[str] = Form(...)):
    # Сохраняем загруженный файл
    file_location = f"/tmp/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    
    # Выполняем транскрибацию аудио файла
    transcription = transcribe(file_location)
    generations = []

    # Печатаем строки 
    for line in strings:
        prompt = (
            f'Проверка регламента по тексту. Текст: Машинист Калтынбаев, на поез ой на маневровую переходите на УКВ. '
            f'На УКВ переходим, машинист (не понятно) Регламент: Перед отправлением поезда с железнодорожной станции '
            f'при разрешающем показании выходного (маршрутного) светофора машинист и помощник машиниста обязаны '
            f'выполнить регламент “Минута готовности” в виде диалога, при котором помощник машиниста контролирует '
            f'и объявляет машинисту: о наличии поездных документов и бланка предупреждений. Ответ (да - если '
            f'соответствует, фрагмент с ошибкой - если не соответствует): да. Проверка регламента по тексту. '
            f'Текст: Машинист поезда № 2208 на приближении к станции Знойное. Слушаю Вас, машинист поезда 2120 '
            f'Лепихин. Регламент: В переговорах нельзя употрелять имена и фамилии. Ответ (да - если соответствует, '
            f'фрагмент с ошибкой - если не соответствует): ...машинист поезда №2120 Лепихин.... Проверка соответствия '
            f'текста регламенту. Текст: {transcription} Регламент: {line}\nОтвет (да - если соответствует, текст c '
            f'ошибкой, если не соответствует):'
        )
        
        generation = generate_text(prompt)

        result = generation[len(prompt):].strip()
        generations.append(result)

    # Возвращаем результат в JSON
    return JSONResponse(content={"transcription": transcription, "generations": generations})
