import psutil
import requests
import time

# Токен вашего бота, полученный у BotFather
TOKEN = ""

# ID чата, куда будут отправляться сообщения
CHAT_ID = ""

# URL для отправки сообщений через API Telegram
URL = "https://api.telegram.org/bot{}/sendMessage".format(TOKEN)

while True:
    # Получаем данные о нагрузке на систему
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    network_io_counters = psutil.net_io_counters()
    processes = []

    for process in psutil.process_iter():
        try:
            process_name = process.name()
            process_cpu_percent = process.cpu_percent()
            process_memory_percent = process.memory_percent()
            processes.append("{}: CPU {}%, Mem {}%".format(process_name, process_cpu_percent, process_memory_percent))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Формируем сообщение с данными о нагрузке
    message = "CPU: {}%\nMemory: {}%\nBytes sent: {}\nBytes recv: {}\n\nProcesses:\n{}".format(cpu_percent, memory_percent, network_io_counters.bytes_sent, network_io_counters.bytes_recv, "\n".join(processes))

    # Отправляем сообщение через API Telegram
    requests.post(URL, data={"chat_id": CHAT_ID, "text": message})

    # Ждем 1 минуту перед отправкой следующего сообщения
    time.sleep(60)