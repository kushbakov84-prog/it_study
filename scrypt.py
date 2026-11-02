name = "Beksutan"
print(f"Привет, {name}! Твой первый скрипт на Python работает.")
server_name = "ai-workers-01"
ram_gb = 16
is_active = True
report_text = f"Отчет по серверу {server_name}:\nПамять: {ram_gb} GB\nАктивен: {is_active}\n"
with open("server_report.txt", "w") as file:
    file.write(report_text)
print("Репорт выполнился, проверь новый файл!")


