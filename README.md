## Проект по автоматизации сайта "Saucedemo.com"


## Используемые инструменты
<div>
<img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" title="python" alt="python" width="40" height="40"/>&nbsp
<img src="https://user-images.githubusercontent.com/25181517/184117132-9e89a93b-65fb-47c3-91e7-7d0f99e7c066.png" title="pytest" alt="pytest" width="40" height="40"/>&nbsp
<img src="https://user-images.githubusercontent.com/25181517/184103699-d1b83c07-2d83-4d99-9a1e-83bd89e08117.png" title="selene" alt="selene" width="40" height="40"/>&nbsp
<img src="https://selenoid.autotests.cloud/favicon.ico" title="selenoid" alt="selenoid" width="40" height="40"/>&nbsp
<img src="https://img.icons8.com/?size=100&id=3tC9EQumUAuq&format=png&color=000000" title="github" alt="github" width="40" height="40"/>&nbsp
<img src="https://user-images.githubusercontent.com/25181517/179090274-733373ef-3b59-4f28-9ecb-244bea700932.png" title="jenkins" alt="jenkins" width="40" height="40"/>&nbsp
<img src="https://camo.githubusercontent.com/501c9d05b6660ba5e1a8753b8461e60d7ff1614656102c254ab800e14a6b19fa/68747470733a2f2f616c6c7572657265706f72742e6f72672f7075626c69632f696d672f616c6c7572652d7265706f72742e737667" title="allure" alt="allure" width="40" height="40"/>&nbsp
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pycharm/pycharm-original.svg" title="pycharm" alt="pycharm" width="40" height="40"/>&nbsp
<img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" title="telegram" alt="telegram" width="40" height="40"/>&nbsp
</div>

## Список автоматизированных тест-кейсов:
1. Проверка успешной авторизации.
2. Проверка отображения сообщения об ошибке при попытке пройти авторизацию с аккаунта заблокированного пользователя.
3. Проверка добавления всех товаров в корзину.
4. Проверка удаления всех товаров из корзины (очистка корзины).
5. Проверка перехода на страницу со списком товаров после нажатия на кнопку "Continue Shopping".
6. Проверка корректного вычисления значения в поле "Item Total".
7. Проверка перехода на страницу оплаты товаров после нажатия на кнопку "Checkout".
8. Проверка прохождения полного цикла покупки товара.

## Запуск тестов и получение отчета

### **Локально**

<details><summary>1. Склонировать репозиторий</summary>

```
git clone https://github.com/msborja/HW14
```
</details>

<details><summary>2. Установить зависимости и запустить тесты</summary>

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
</details>

<details><summary>3. Получить отчет о прохождении тестов в allure</summary>

```
allure serve allure-results/
```
</details>

<details><summary>4. После выполнения команды откроется браузер с отчетом</summary>
    
<img src="resources/report_allure.png">

</details>

### **Удалённо**

Удаленный запуск автотестов осуществляется при помощи Jenkins. Для этого необходимо выполнить следующие действия:

1. Открыть [проект на Jenkins](https://jenkins.autotests.cloud/job/qa_guru_python_hw_14/)

<details><summary>2. Нажать на кнопку "Build with Parameters"</summary>

<img src="resources/jenkins.png">

</details>

<details><summary>3. Дождаться окончания выполнения автотестов и нажать на иконку allure <img src="https://camo.githubusercontent.com/501c9d05b6660ba5e1a8753b8461e60d7ff1614656102c254ab800e14a6b19fa/68747470733a2f2f616c6c7572657265706f72742e6f72672f7075626c69632f696d672f616c6c7572652d7265706f72742e737667" title="allure" alt="allure" width="20" height="20"/> для просмотра отчета</summary>

<img src="resources/jenkins2.png">

</details>

## **Дополнительно**

Реализована отправка результатов тестирования в Telegram <img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" title="telegram" alt="telegram" width="20" height="20"/>  
<details><summary>Пример отчета</summary>

<img src="resources/report_telegram.png" alt="report Telegram">

</details>

<details><summary>Пример видеоотчета о прохождении автотестов</summary>

<img src="resources/video_example.gif" alt="gif example report">

</details>