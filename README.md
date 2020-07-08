SUAIbot documentation

Данный бот предназначен для автоматизации отметки посечений лекционнаых занятий в дискорде.
Основые команды:

!start бот отмечает студентов
	
		Бот отправляет сообщение и ставит реакцию, 
		студентам нужно лишь нажать на эту реакцию (☑), 
		через 3 минуты все данные, которые присутствуют в сообщении
		(студенты которые поставили реакции) обрабатываются, 
		и соответственно заполняется гугл таблица. После истечения таймера 
		бесполезно добавлять реакции. Список пользователей, 
		поставивших реакции отправляются в закрытый чат 
		(определенный идентификатора как и роли см. ниже), 
		так же отпраляется 
		список пользователей с неправильными никнеймами. 
		Данная команда доступна только пользователем с ролью имеющией 
		определенный идентификатор (который можно узнать щелкнув
		на правой кнопкой мыши на роль (копировать ID) в 
		режиме разработчика (всключается в настройках))
Запуск 

	python bot.py
Установка необходимых дополнительных библиотек:

	pip install discord.py
	pip install gspread oauth2client
Более подробную инструкцию для работы с таблицами можно узнать по ссылке : 

https://www.youtube.com/watch?v=cnPlKLEGR7E
