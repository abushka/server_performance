# server_performance

скрипт для отправки нагрузки на сервер через телеграмм, мне это нужно было потому, что на сервак проник майнер Perfctl (о котором я тогда не подозревал),
и когда я заходил по ssh чтобы проверить что так сильно нагружает процессор - майнер останавливал работу и не давал себя спалить,
поэтому я решил не заходить через ssh и проверять нагрузку, а просто запустил скрипт в фоновом режиме командой

`nohup python3 server_notifications.py > output.log`

дабы майнер не останавливался и не спалил что проверяют нагрузку :)
