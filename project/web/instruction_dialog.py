import streamlit as st


html = """
        <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { font-size: 24px; }
                h2 { font-size: 20px; margin-top: 20px; }
                h3 { font-size: 18px; margin-top: 15px; }
                ul { margin: 10px 0; }
            li { margin-bottom: 5px; }
        </style>
        <h1>Застосунок для Прогнозування Відтоку Клієнтів!</h1>
        
        <h2>1. Інструкція Користувача</h2>
        <p>Цей додаток дозволяє аналізувати клієнтські дані та визначати ймовірність припинення використання послуг.</p>
        
        <h2>2. Вимоги до Системи</h2>
        <p>Перед початком роботи переконайтеся, що у вас встановлено Docker та Docker Compose для запуску проекту в контейнеризованому середовищі.</p>
        
        <h2>3. Запуск Системи</h2>
        <ul>
            <li>
                <strong>Завантаження проєкт:</strong>
                <ul>
                    <li>Завантажте архів з кодом проєкт або клонуйте репозиторій за допомогою Git.</li>
                </ul>
            </li>
            <li>
                <strong>Запуск Docker Compose:</strong>
                <ul>
                    <li>Відкрийте термінал у директорії проєкт.</li>
                    <li>Виконайте команду <code>docker-compose up</code> для розгортання додатку з Docker контейнера.</li>
                </ul>
            </li>
        </ul>
        
        <h2>4. Використання Системи</h2>
        <ul>
            <!--li>
                <strong>Доступ до додатку:</strong>
                <ul>
                    <li>Перейдіть за посиланням до хмарного додатку через веб-браузер.</li>
                    <li>Авторизуйтеся, якщо це необхідно.</li>
                </ul>
            </li-->
            <li>
                <strong>Головна сторінка:</strong>
                <ul>
                    <li>Інструкція Користувача: Доступ до інструкції користувача здійснюється натисканням на кнопку "Інструкція користування".</li>
                    <li>Початок Аналізу: Для прогнозування відтоку клієнтів натисніть на кнопку "Почати аналіз!".</li>
                </ul>
            </li>
        </ul>
        
        <h2>5. Сторінка прогнозування відтоку клієнтів (за замовчуванням обрана сторінка "Одиночне прогнозування")</h2>
        <ul>
            <li>
                <strong>Бокова панель:</strong>
                <ul>
                    <li>Кнопка "Повернутися на головну" відкриває головну сторінку.</li>
                    <li>Кнопка "Інструкція користування" відкриває інструкцію користувача.</li>
                    <li>Кнопка "Тестовий файл" відкриває зразок датасету для завантаження.</li>
                    <li>Кнопка "Вимоги показників введення" відображає таблицю з мінімально та максимально допустимими значеннями полів для введення у форму одиночного прогнозування.</li>
                    <li>Кнопка "Оновити" оновлює дані на сторінці.</li>
                </ul>
            </li>
            <li>
                <strong>Одиночне Прогнозування:</strong>
                <ul>
                    <li>Вибір цієї опції дозволяє прогнозувати відтік для одного клієнта. Дозволяє вводити декількох клієнтів по черзі і відображати статистику.</li>
                    <li>Для вибору одиночного прогнозування клієнтів натисніть вкладку "Одиночне прогнозування".</li>
                </ul>
            </li>
            <li>
                <strong>Прогнозування для списку користувачів:</strong>
                <ul>
                    <li>Вибір цієї опції дозволяє прогнозувати відтік клієнтів використовуючи датасет.</li>
                    <li>Для визначення відтоку клієнтів використовуючи датасет натисніть вкладку "Прогнозування для списку користувачів".</li>
                </ul>
            </li>
        </ul>
        
        <h2>6. Сторінка: Одиночне Прогнозування</h2>
        <ul>
            <li>
                <strong>Введення Даних:</strong>
                <ul>
                    <li>Щоб вибрати модель прогнозування, натисніть на поле "Оберіть модель для використання" та у випадаючому меню виберіть потрібну модель прогнозування. Модель "decision_tree" встановлена за замовчуванням.</li>
                    <li>Введіть дані клієнта у відповідні поля та натисніть на кнопку 'Прогнозувати' для отримання результатів.</li>
                </ul>
            </li>
            <li>
                <strong>Результати:</strong>
                <ul>
                    <li>Результати будуть відображені у таблиці "Всі результати прогнозування".</li>
                    <li>Щоб зберегти дані прогнозування встановіть пойнтер мишки в правому верхньому куті таблиці "Всі результати прогнозування" і натисніть Download as CSV.</li>
                </ul>
            </li>
            <li>
                <strong>Графічне відображення результатів:</strong>
                <ul>
                    <li>Графічні відображення результатів прогнозування будуть зображені на графіку "Розподіл ймовірності відтоку".</li>
                    <li>Для перегляду й оцінки даних щодо обраної моделі натисніть на кнопку "Переглянути важливість ознак".</li>
                </ul>
            </li>
            <li>Щоб оновити дані на сторінці натисніть на кнопку "Оновити" в боковій панелі.</li>
        </ul>
        
        <h2>7. Сторінка: Прогнозування для списку користувачів</h2>
        <ul>
            <li>
                <strong>Введення Даних:</strong>
                <ul>
                    <li>Щоб перейти на сторінку прогнозування для списку користувачів натисніть на кнопку "Прогнозування для списку користувачів".</li>
                    <li>Щоб вибрати модель прогнозування, натисніть на поле "Оберіть модель для використання" та у випадаючому меню виберіть потрібну модель прогнозування. Модель "decision_tree" встановлена за замовчуванням.</li>
                </ul>
            </li>
            <li>
                <strong>Завантаження Датасету:</strong>
                <ul>
                    <li>Використайте поле 'Drag and drop file here' для завантаження датасету методом 'drag and drop' або натисніть на кнопку 'Browse files' для завантаження датасету з локального середовища.</li>
                </ul>
            </li>
            <li>
                <strong>Формат Датасету:</strong>
                <ul>
                    <li>Датасет повинен бути у форматі .csv.</li>
                    <li>Датасет повинен містити наступні поля:</li>
                    <ul>
                        <li><code>id</code>: ідентифікатор клієнта.</li>
                        <li><code>is_tv_subscriber</code>: інформація про підписку на телебачення.</li>
                        <li><code>is_movie_package_subscriber</code>: інформація про підписку на пакети фільмів.</li>
                        <li><code>subscription_age</code>: тривалість підписки.</li>
                        <li><code>remaining_contract</code>: термін, що залишився до кінця контракту.</li>
                        <li><code>download_avg</code>: середній об'єм завантаження.</li>
                        <li><code>upload_avg</code>: середній об'єм відвантаження.</li>
                        <li><code>download_over_limit</code>: перевищення ліміту завантаження.</li>
                    </ul>
                </ul>
            </li>
            <li>
                <strong>Аналіз та Результати:</strong>
                <ul>
                    <li>Завантажте датасет та натисніть на кнопку "Зробити прогнозування" для обробки даних та отримання результатів.</li>
                </ul>
            </li>
            <li>
                <strong>Результати:</strong>
                <ul>
                    <li>Результати будуть відображені у таблиці "Вірогідність відтоку" та на графіку "Розподіл ймовірності відтоку".</li>
                    <li>Щоб зберегти дані прогнозування встановіть пойнтер мишки в правому верхньому куті таблиці "Вірогідність відтоку" і натисніть Download as CSV.</li>
                </ul>
            </li>
            <li>
                <strong>Графічне відображення результатів:</strong>
                <ul>
                    <li>Для перегляду й оцінки даних щодо обраної моделі натисніть на кнопку "Переглянути важливість ознак".</li>
                </ul>
            </li>
            <li>Щоб оновити дані на сторінці натисніть на кнопку "Оновити" в боковій панелі зліва.</li>
        </ul>
        
        <h2>8. Опис Категорій відтоку</h2>
        <ul>
            <li>
                <span style="color: green">Низька</span>: від 0 до 33%
            </li>
            <li>
                <span style="color: yellow">Середня</span>: від 34% до 66%
            </li>
            <li>
                <span style="color: red">Висока</span>: від 67% до 100%
            </li>
        </ul>
    """


@st.dialog(" ", width="large")  # instruction dialog window
def show_instruction_dialog():
    st.markdown(html, unsafe_allow_html=True)
