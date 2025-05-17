import telebot
from telebot import types
import random
import json
import requests
import threading

API = 'db53663bae2e3b33d925fcb7279e77a2'
bot = telebot.TeleBot('')
user_data={}
#факты 
FACTS = [
    "🐕 **Собаки-космонавты Белка и Стрелка** (1960) стали первыми, кто вернулся из орбитального полёта живым. Стрелка позже родила здоровых щенков!",
    "🚀 **Первый искусственный спутник** (1957) — «Спутник-1» весил всего 84 кг и передавал легендарные сигналы «бип-бип», которые ловили радиолюбители по всему миру.",
    "🌕 **Тайна обратной стороны Луны** (1959) — Советская станция «Луна-3» впервые в истории сфотографировала невидимую с Земли сторону Луны, открыв миру совершенно новый ландшафт.",
    "👨‍🚀 **108 минут, изменившие мир** (1961) — Полёт Гагарина длился меньше двух часов, но навсегда сделал СССР первопроходцем космоса. Его позывной «Кедр» знала вся планета!",
    "🛰️ **Спутник-шпион с сюрпризом** (1960-е) — Советские аппараты «Зенит» возвращали капсулы с плёнкой, которые искали в тайге с вертолётов. Однажды медведи приняли капсулу за мёд и повредили её!",
    "🌌 **Рекорд Венеры** (1970) — «Венера-7» совершила первую мягкую посадку на адской поверхности Венеры (465°C!) и передавала данные 23 минуты — подвиг инженерной мысли.",
    "🔭 **Космический телескоп-невидимка** (1983) — «Астрон» с зеркалом 80 см стал крупнейшим ультрафиолетовым телескопом своего времени и открыл тысячи новых галактик.",
    "🤖 **Автоматический космический челнок** (1988) — «Буран» совершил единственный полёт вообще без экипажа, в полностью автоматическом режиме — технология, до сих пор непревзойдённая на Западе.",
    "👾 **Луноходы с характером** (1970-е) — Советские луноходы могли «просыпаться» по команде с Земли, грелись ядерным нагревателем и оставляли на Луне «автографы» — зеркала для лазерной локации.",
    "🛰️ **Секретный двойник** (1970-е) — Каждый научный спутник серии «Космос» на деле мог быть военным, а их настоящие задачи рассекречивают только сейчас!",
    "🌠 **Космическая станция-долгожитель** (1986-2001) — «Мир» проработала в 3 раза дольше запланированного срока и стала первым «космическим домом» для международных экипажей.",
    "⚡ **Энергия ядра в космосе** (1960-е) — СССР запускал спутники с ядерными реакторами на борту. «Космос-1867» проработал на орбите целый год!",
    "🧪 **Космическая алхимия** (1990-е) — На станции «Мир» выращивали идеальные кристаллы полупроводников, которые невозможно создать в земных условиях.",
    "🛸 **Охота за НЛО** (1978) — Советские ВВС имели секретную инструкцию для пилотов по взаимодействию с «аномальными воздушными явлениями» — документ рассекретили в 2000-х.",
    "🌑 **Лунные роботы-разведчики** (1970) — Перед отправкой луноходов СССР сбросил на Луну два «шагающих» аппарата ПрОП-М — они напоминали маленькие стиральные машины на лыжах!",
    "🚀 **Ракета, опередившая время** (1960-е) — «Н-1» могла бы доставить советских космонавтов на Луну, но её двигатели (30 одновременно!) оказались слишком сложными для своей эпохи."
]
@bot.message_handler(commands=['start'])
def button_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Интересный факт 🚀")
    markup.add(btn1)
    btn2 = types.KeyboardButton("Узнать погоду за бортом")
    markup.add(btn2)
    btn3 = types.KeyboardButton("Сыграть в космическую викторину")
    markup.add(btn3)
    bot.send_message(message.chat.id, "Привет, космический исследователь! Я расскажу тебе о великих достижениях СССР в космосе. 🌌\n\n Выбери одну из кнопок снизу, которую ты хочешь", reply_markup = markup)
    
@bot.message_handler(func=lambda message:message.text == 'Интересный факт 🚀')
def send_fact(message):
    fact = random.choice(FACTS)
    bot.send_message(message.chat.id, f"📡 <b>Космический факт СССР:</b>\n\n{fact}", parse_mode="HTML")
#погода
@bot.message_handler(func=lambda message: message.text == "Узнать погоду за бортом")
def ask_city(message):
    bot.send_message(message.chat.id, "Введите название <b>города</b> мимо, которого мы пролетаем", parse_mode="HTML")
    bot.register_next_step_handler(message,send_weather)
def send_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f"Сейчас погода: {temp}℃")
    else:
        bot.reply_to(message, "Возможно, этот город находится не на Земле. Введите корректный город)")
        bot.register_next_step_handler(message, ask_city)

#викторина
@bot.message_handler(func=lambda message:message.text == "Сыграть в космическую викторину")
def choose_tema(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn_astronauts = types.KeyboardButton("Космонавты")
    btn_satellites = types.KeyboardButton("Спутники")
    btn_stations = types.KeyboardButton("Станции")
    btn_tech = types.KeyboardButton("Технологии")
    markup.add(btn_astronauts, btn_satellites, btn_stations, btn_tech)
    bot.send_message(message.chat.id, 'Выберите тему викторины', reply_markup=markup)
def load_questions(topic):
    with open(f"{topic}.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        questions = data["questions"]
        # сложность: 6 легких, 8 средних, 6 сложных, хз так тоже хорошо
        return {
            "easy": questions[:6],
            "medium": questions[6:14],
            "hard": questions[14:]
        }

@bot.message_handler(func=lambda msg: msg.text in ["Космонавты", "Спутники", "Станции", "Технологии"])
def start_quiz(message):
    user_id = message.from_user.id
    topic = message.text.lower()
    #надо
    user_data[user_id] = {
        "topic": topic,
        "score": 0,
        "questions": load_questions(topic),
        "current_question": None,
        "timer": None
    }
    ask_difficulty(message.chat.id, user_id)

def ask_difficulty(chat_id, user_id):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    easy_btn = types.KeyboardButton("🟢 Лёгкий")
    medium_btn = types.KeyboardButton("🟡 Средний")
    hard_btn = types.KeyboardButton("🔴 Сложный")
    markup.add(easy_btn, medium_btn, hard_btn)
    # сколько вопросов осталось, чисто визуальчик
    questions_left = ""
    for diff, questions in user_data[user_id]["questions"].items():
        if questions:
            emoji = "🟢" if diff == "easy" else "🟡" if diff == "medium" else "🔴"
            questions_left += f"{emoji} {len(questions)} | "
    bot.send_message(chat_id,f"Выбери сложность следующего вопроса:\n(Осталось: {questions_left[:-2]})",reply_markup=markup)
@bot.message_handler(func=lambda msg: msg.text in ["🟢 Лёгкий", "🟡 Средний", "🔴 Сложный"])
def set_difficulty(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        return choose_tema(message)
    difficulty_map = {
        "🟢 Лёгкий": "easy",
        "🟡 Средний": "medium",
        "🔴 Сложный": "hard"
    }
    difficulty = difficulty_map[message.text]
    
    # проверка есть ли вопросы выбранной сложности, крч надо просто всё проверять как в нормальном боте иначе габелла
    if not user_data[user_id]["questions"][difficulty]:
        bot.send_message(message.chat.id, f"Вопросы уровня {message.text} закончились!")
        return ask_difficulty(message.chat.id, user_id)
    
    # просто первый вопрос берём
    question = user_data[user_id]["questions"][difficulty].pop(0)
    user_data[user_id]["current_question"] = {
        "question": question,
        "difficulty": difficulty
    }
    send_question(message.chat.id, user_id)

def send_question(chat_id, user_id):
    question_data = user_data[user_id]["current_question"]
    question = question_data["question"]
    difficulty = question_data["difficulty"]
    # создаем кнопки с вариантами (перемешиваем порядок), вдруг гога сделал так чтобы правильный ответы были только первые
    options = question["options"]
    random.shuffle(options)
    markup = types.InlineKeyboardMarkup()
    row = []
    for i, option in enumerate(options):
        callback_data = f"ans_{i}_{option}"
        row.append(types.InlineKeyboardButton(option, callback_data=callback_data))
        if len(row) == 2:  # 2 кнопки в ряд
            markup.row(*row)
            row = []
    #тут подсказал дипсик что так надо сделать, добавляем оставшиеся кнопки, если нечетное количество
    if row:
        markup.row(*row)
    # отправляем вопрос
    diff_emoji = "🟢" if difficulty == "easy" else "🟡" if difficulty == "medium" else "🔴"
    bot.send_message(chat_id,f"{diff_emoji} Вопрос ({difficulty.capitalize()}):\n\n{question['question']}",reply_markup=markup)
    # запускаем таймер (30 секунд на ответ), этого я рот ебал
    if user_data[user_id].get("timer"):
        user_data[user_id]["timer"].cancel()
    timer = threading.Timer(30.0, timeout_question, args=[chat_id, user_id])
    user_data[user_id]["timer"] = timer
    timer.start()
def timeout_question(chat_id, user_id):
    if user_id in user_data:
        question = user_data[user_id]["current_question"]["question"]
        bot.send_message(chat_id,f"⏰ Время вышло! Правильный ответ: {question['answer']}\n{question['explanation']}")
        ask_difficulty(chat_id, user_id)
@bot.callback_query_handler(func=lambda call: call.data.startswith("ans_"))
def handle_answer(call):
    user_id = call.from_user.id
    if user_id not in user_data:
        return
    # парсим callback_data: ans_индекс_текст
    parts = call.data.split("_")
    selected_idx = int(parts[1])
    selected_text = "_".join(parts[2:])
    question = user_data[user_id]["current_question"]["question"]
    difficulty = user_data[user_id]["current_question"]["difficulty"]
    # останавливаем таймер
    if user_data[user_id].get("timer"):
        user_data[user_id]["timer"].cancel()
    # проверяем ответ + баллы
    if selected_text == question["answer"]:
        points = {"easy": 1, "medium": 3, "hard": 5}[difficulty]
        user_data[user_id]["score"] += points
        response = f"✅ Верно! +{points} баллов"
    else:
        response = f"❌ Неверно! Правильный ответ: {question['answer']}"
    # редактируем сообщение с вопросом (добавляем отметку о ответе)
    try:
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"{call.message.text}\n\n{response}",
            reply_markup=None
        )
    except:
        pass
    # доп инфа
    bot.send_message(call.message.chat.id,f"📚 Пояснение:\n{question['explanation']}\n\nТвой счет: {user_data[user_id]['score']}")
    # проверяем остались ли вопросы
    total_questions_left = sum(len(q) for q in user_data[user_id]["questions"].values())
    if total_questions_left == 0:
        finish_quiz(call.message.chat.id, user_id)
    else:
        ask_difficulty(call.message.chat.id, user_id)

def finish_quiz(chat_id, user_id):
    score = user_data[user_id]["score"]
    topic = user_data[user_id]["topic"]
    
    # "звание" по количеству баллов, прикольная штучка
    if score >= 30:
        rank = "👨‍🚀 Генерал космических войск!"
    elif score >= 20:
        rank = "🛰️ Главный конструктор!"
    elif score >= 10:
        rank = "🚀 Космический инженер!"
    else:
        rank = "🌍 Начинающий исследователь!"
    
    #бэкаемся
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Интересный факт 🚀"))
    markup.add(types.KeyboardButton("Узнать погоду за бортом"))
    markup.add(types.KeyboardButton("Сыграть в космическую викторину"))
    
    bot.send_message(chat_id,
        f"🏆 Викторина завершена!\n\n"
        f"Тема: {topic.capitalize()}\n"
        f"Набрано баллов: {score}\n"
        f"Твое звание: {rank}",reply_markup=markup
    )
    if user_id in user_data:
        del user_data[user_id]
bot.polling(none_stop=True)