import pandas as pd
import numpy as np

print("Запуск ИИ-модуля аналитики данных...")

# 1. Создаем структуру данных с метриками серверов
data = {
    "server_name": ["ai-worker-01", "ai-worker-02", "storage-server", "backup-node"],
    "cpu_load_percent": [88.5, 92.1, 15.4, 8.2],
    "ram_usage_gb": [14.2, 15.8, 4.1, 2.0]
}

# 2. С помощью Pandas превращаем обычные данные в мощную таблицу (DataFrame)
df = pd.DataFrame(data)

# 3. Используем NumPy, чтобы автоматически разметить критический статус нагрузки (более 80%)
df["status"] = np.where(df["cpu_load_percent"] > 80.0, "CRITICAL (High Load)", "OK (Normal)")

# 4. Выводим таблицу в терминал для проверки
print("\n--- Результаты анализа инфраструктуры ---")
print(df)

# 5. Сохраняем таблицу в профессиональный файл отчета CSV
df.to_csv("infrastructure_report.csv", index=False)
print("\nАналитический отчет успешно сохранен в infrastructure_report.csv!")
