# Анализатор служебных переговоров

Репозиторий для хакатона по кейсу "Анализатор служебных переговоров".

## ИИ-сервис

Сервис, который использует модели ИИ, написан на Python. Находится в /aiservice.
Запускается на порту 8000.

Используется две модели с открытым исходным кодом:
- WHISPER (OpenAI) - расшифровка аудио в текст.
- ruGPT3 (Sber) - используется для анализа расшифрованного текста.

Используется SMALL-версии моделей. Запустить можно либо на GPU, либо на CPU (в коде есть проверка на GPU, если он есть - запускается на GPU, иначе на CPU).

Сервис предоставляет API, который принимает аудиофайл в форме и возрващает расшифровку и аналитику по переговорам.

## C#-сервис

Сервис предоставляет API для веб-платформы. Находится в /aspapp. Запускается на порту 5000. 

Более подробное описание Endpoints - Перейти.

Запускается на портах 8080 и 8081.

## NGINX-сервис

Сервис нужен для предоставления сгенерированных статистических файлов пользователю. Запускается на стандартном HTTP-порту (80).

## Frontend

Клиентская часть платформы написана на VueJS. Находится в client. Готовая сборка находится в static_client.

# PHPMyAdmin

В Docker-композиции собирается готовый образ панил управления MySQL - PHPMyAdmin.

Запускается на порту 8080.

