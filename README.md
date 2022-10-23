# MyWorkout-Web
Выполненное задание по разработке приложения, взаимодействующего с спроектированной базой данных, по дисциплине "Базы данных"

## Запуск
Для запуска проекта необходимо:
1. Склонировать проект с репозитория:  
```git clone https://github.com/MatweyL/MyWorkout-Web.git```  
или  
```git clone git@github.com:MatweyL/MyWorkout-Web.git```
2. Если есть запущенные контейнеры с MySQL, остановить их. Запустить контейнер с СУБД с помощью команды ```docker-compose up```
3. Создать в корне проекта файл *.env*, в котором, согласно .env.template, ввести данные подключения к БД
4. Запустить проект с помощью команды ```python main.py```

## Примеры интерфейса

- Главная страница
![image](https://user-images.githubusercontent.com/74009572/196236094-88d21444-617c-4490-a11d-180799e74e1f.png)

- Страница авторизации
![image](https://user-images.githubusercontent.com/74009572/196236272-6aeb4dd7-eaca-44cf-b275-e53d04539b55.png)

- Страница упражнений
![image](https://user-images.githubusercontent.com/74009572/196236470-c392a9fc-56c6-4843-82c4-706d9dcb5706.png)

- Страница тренировок
![image](https://user-images.githubusercontent.com/74009572/196236517-260633e1-7e28-4ef6-9534-9e6af8e81e64.png)

- Страница создания упражнений
![image](https://user-images.githubusercontent.com/74009572/196236549-9f2753e2-8bde-44ac-9fde-d973d642c03d.png)

- Страница добавления мышц к упражнениям
![image](https://user-images.githubusercontent.com/74009572/196236654-bf1b4335-d78d-4048-baa7-b3a86d61e72f.png)

- Страница отображения упражнения
![image](https://user-images.githubusercontent.com/74009572/196236762-59e08491-eaf7-4353-84f2-ef65538c450f.png)

- Страница добавления упражнения в тренировку
![image](https://user-images.githubusercontent.com/74009572/196236827-469f99f1-9ead-4338-83de-212643eea8d6.png)

- Страница отображения тренировки
![image](https://user-images.githubusercontent.com/74009572/196236856-e5d23427-7221-4055-89bf-c936fa31366d.png)
