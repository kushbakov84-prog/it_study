# Список наших серверов
servers = ["ai-worker-01", "ai-worker-02", "storage-server"]

# Перебираем серверы
for server in servers:
    if server.startswith("ai"):
        # Задаем имя файла динамически для каждого ИИ-сервера
        filename = f"report_{server}.txt"

        # Создаем текст лога
        log_message = f"Статус: ИИ-нода {server} активна.\nМониторинг запущен успешно.\n"

        # Записываем лог в индивидуальный файл (8 пробелов отступа!)
        with open(filename, "w") as file:
            file.write(log_message)

        print(f"Создан отчет для сервера: {filename}")



