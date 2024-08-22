import pywhatkit
import json
import time

with open('phones.json', encoding='utf-8') as file:
    list_of_number = json.load(file)

# with open('photo.png', 'rb') as r:
#     photo = r.read()
photo = 'photo1.jpeg'
def send_message_inst():
    # Shorten the message to prevent URL length error
    message = """
Бесплатная компьютерная диагностика для пользователей приложения Орра !
Приложение Oppa для быстрого поиска автозапчастей 📲
Скачивайте на
🍏ios
🤖android

https://www.oppa.kg/
        """

    for k, v in list_of_number.items():
        phone = v['phone']
        pywhatkit.sendwhats_image(phone, photo , message, tab_close=True)
        if k == 1600:
            break
        time.sleep(30)

def main():
    send_message_inst()

if __name__ == '__main__':
    main()
