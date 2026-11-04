import pandas as pd
from transformers import pipeline

print("Загрузка ИИ-модели анализа текста...")
# Инициализируем готовую мини-нейросеть для анализа тональности текста
classifier = pipeline("sentiment-analysis", model="bhadresh-savani/distilbert-base-uncased-emotion")

# Наш набор логов и жалоб от пользователей
logs = [
    "The server is running incredibly fast, I love it!",
    "Database connection failed again. This is terrible.",
    "I am worried about the recent security update.",
    "Everything is working fine and stable."
]

print("ИИ анализирует текст...")
results = classifier(logs)

# Собираем результаты в красивую таблицу с помощью Pandas
analyzed_data = []
for text, result in zip(logs, results):
    analyzed_data.append({
        "Text": text,
        "Emotion": result["label"],
        "Confidence": round(result["score"], 2)
    })

df = pd.DataFrame(analyzed_data)

print("\n--- Результаты анализа эмоций ИИ ---")
print(df)

# Сохраняем в CSV
df.to_csv("ai_emotion_report.csv", index=False)
print("\nОтчет сохранен в ai_emotion_report.csv!")
