import configuration
import requests
import data

#Создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDERS,
                         json=order_body)

#Сохранение трек-номер заказа
def get_new_track():
    responce = post_new_order(data.order_body)
    track = responce.json()["track"]
    return track

#Получение заказа по трек-номеру

def get_order_body(track):
    params_with_track= {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GETTING_INFORMATION_BY_ORDER,
                        params=params_with_track)