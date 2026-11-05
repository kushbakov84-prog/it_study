from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

print("Инициализация ИИ-микросервиса...")
# 1. Загружаем нейросеть в память сервера при старте
classifier = pipeline("sentiment-analysis", model="bhadresh-savani/distilbert-base-uncased-emotion", device="cpu")

# 2. Создаем веб-приложение FastAPI
app = FastAPI(title="ИИ Анализатор Эмоций Логов")

# Описываем структуру входящего запроса (ИИ ожидает текст)
class LogRequest(BaseModel):
    text: str

# 3. Создаем стартовую страницу для проверки работоспособности
@app.get("/")
def read_root():
    return {"status": "AI Server is running smoothly"}

# 4. Создаем сетевой маршрут (эндпоинт) для предсказаний ИИ
@app.post("/predict")
def predict_emotion(request: LogRequest):
    try:
        # Прогоняем текст через нейросеть
        prediction = classifier(request.text)[0]
        return {
            "text": request.text,
            "emotion": prediction["label"],
            "confidence": round(prediction["score"], 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
