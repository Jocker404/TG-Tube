# TG-Tube
Bot Telegram Server para descargar música y videos de YouTube además de files de github con registro de eventos de error y registro en base de datos de las entradas.

# Plataforma Windows
+ Testeado sobre Windows 10

# Dependencias de TG-Tube
+ pip install pysqlite
+ pip install moviepy
+ pip install pafy
+ pip install python-telegram-bot
+ pip install colorama

# Uso de TG-Tube
1º Crear un bot por ejemplo BotFather colocar en el DownYotubeBotTelegram.py la API del bot.
2º Ejecutar el DownYotubeBotTelegram.py si la data base file no existe creara una al igual al file logg.
3º Los archivos descargados se borran de la carpeta donde se ejecuta el server del bot.
4º Los registros de Errores se guardan en un logger.dat
5º Los registros de usuarios que usan el bot se guandan en la database log_telegram_download.sqlite

# Licencia AGPL
