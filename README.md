Запросы расположены в файле Base.sql 

Задание 1 Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных. Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).

запрос:

      SELECT c.login, COUNT(o.id) AS "deliveryCount" 
      FROM "Couriers" AS c 
      LEFT JOIN "Orders" AS o ON c.id = o."courierId" 
      WHERE o."inDelivery" = true 
      GROUP BY c.login;
Скриншот результата запроса sql task/sql task2  ( /Users/Pavel/PycharmProjects/Diploma)

Задание 2

Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно. Для этого: выведи все трекеры заказов и их статусы. Статусы определяются по следующему правилу: Если поле finished == true, то вывести статус 2. Если поле canсelled == true, то вывести статус -1. Если поле inDelivery == true, то вывести статус 1. Для остальных случаев вывести 0.

запрос:

       SELECT track, 
          CASE 
        WHEN finished = true THEN 2 
        WHEN cancelled = true THEN -1 
        WHEN "inDelivery" = true THEN 1 
  ELSE 0 END AS status 
      FROM "Orders";
Скриншот результата запроса Base_request2 sql.png (директория \/Users/Pavel/PycharmProjects/Diploma)

Сдача второй части финального проекта
Для запуска этого пакета тестов должны быть установлены:

интерпретатор Python и среда разработки PyCharm
среда тестирования Pytest, библиотека requests
запущен сервер serverhub.praktikum-services.ru в локальном режиме
после запуска сервера его url должен быть внесён в файл configuration.py в следующую строку:
URL_SERVICE = "https://b43eb7af-d649-47aa-bb81-340f7a6e8a43.serverhub.praktikum-services.ru"
Запуск всех тестов в пакете выполняется командой test_order.py

Для выполнения запросов для БД должен быть установлен Cyg Terminal. Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent. Пароль: smith.
