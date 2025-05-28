import telebot
from telebot import types
import random
import json
import requests
import threading
import time
import os
API = 'db53663bae2e3b33d925fcb7279e77a2'
bot = telebot.TeleBot('#your token')
user_data = {}

GIFS = [
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa29paWhiajY3N29tNzdzbmtqMjU2ZXljNTFoeDhiaHprcHo3ZWo4bCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/9tx0gy37p7oXu/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa29paWhiajY3N29tNzdzbmtqMjU2ZXljNTFoeDhiaHprcHo3ZWo4bCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oKIPtjElfqwMOTbH2/giphy.gif",
    "https://media.giphy.com/media/l0IyjcSmE0QPTBhAs/giphy.gif",
    "https://media.giphy.com/media/GuFALVnrfpNhm/giphy.gif",
    "https://media.giphy.com/media/5yaou1jFxTV6M/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa29paWhiajY3N29tNzdzbmtqMjU2ZXljNTFoeDhiaHprcHo3ZWo4bCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/kiWlpxD6hXmvTL8dio/giphy.gif",
    "https://media.giphy.com/media/3o7TKCTt7cNHg10utO/giphy.gif",
    "https://media.giphy.com/media/3o7TKWvwyGpgtlxQFq/giphy.gif",
    "https://media.giphy.com/media/yGgdwo7YfmrNS/giphy.gif",
    "https://media.giphy.com/media/xT0BKEksASgc4OJGxy/giphy.gif",
    "https://media.giphy.com/media/tdC6N1RKNp4swre2JY/giphy.gif",
    "https://media.giphy.com/media/GyJ8p0Um850ic/giphy.gif",
    "https://media.giphy.com/media/YRzQnWzbn4WIxd3ZYx/giphy.gif",
    "https://media.giphy.com/media/xT39CTrFW4nHLdBPpu/giphy.gif",
    "https://media.giphy.com/media/SVCSsoKU5v6ZJLk07n/giphy.gif",
    "https://media.giphy.com/media/Tpkr2CSADfZwJUwTlD/giphy.gif"
]

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

sent_facts = {}

stats_file = "user_stats.json"
def load_stats():
    if os.path.exists(stats_file):
        with open(stats_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
def save_stats(stats):
    with open(stats_file, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
user_stats = load_stats()

QUOTES = [
    "«Поехали!» — Юрий Гагарин",
    "«Земля — колыбель разума, но нельзя вечно жить в колыбели.» — К.Э. Циолковский",
    "«Увидеть Землю из космоса — значит понять, что мы все одна семья.» — Алексей Леонов",
    "«Дорога в космос открыта!» — Сергей Королёв",
    "«Я — советский человек, и этим горжусь!» — Валентина Терешкова",
    "«Космос — это будущее человечества.» — Сергей Королёв",
    "«В космосе нет дорог, есть только направления.» — Алексей Леонов",
    "«Я вижу Землю! Она такая красивая!» — Юрий Гагарин",
    "«Космос — это не так далеко, как кажется.» — Валентина Терешкова",
    "«Главное — мечтать и верить!» — Валентина Терешкова"
]

PLANET_WEATHER = {
    "Меркурий": {"desc": "Температура днём до +430°C, ночью до -180°C. Атмосферы почти нет.", "temp": "+430°C / -180°C"},
    "Венера": {"desc": "Плотная атмосфера, давление в 90 раз выше земного, температура около +470°C, кислотные облака.", "temp": "+470°C"},
    "Земля": {"desc": "Умеренная температура, вода в жидком виде, разнообразная погода.", "temp": "-90°C до +60°C"},
    "Марс": {"desc": "Тонкая атмосфера, частые пылевые бури, температура от -140°C до +30°C.", "temp": "-140°C до +30°C"},
    "Юпитер": {"desc": "Газовый гигант, сильные ветры, Большое Красное Пятно — гигантский шторм.", "temp": "-145°C"},
    "Сатурн": {"desc": "Газовый гигант, мощные ветры, метановые облака.", "temp": "-178°C"},
    "Уран": {"desc": "Очень холодно, сильные ветры, атмосфера из водорода, гелия и метана.", "temp": "-224°C"},
    "Нептун": {"desc": "Самые сильные ветры в Солнечной системе, очень холодно.", "temp": "-218°C"},
    "Плутон": {"desc": "Карликовая планета, температура около -230°C, разрежённая атмосфера из азота и метана.", "temp": "-230°C"},
    "Европа": {"desc": "Спутник Юпитера, ледяная поверхность, возможный подлёдный океан, температура около -160°C.", "temp": "-160°C"},
    "Титан": {"desc": "Спутник Сатурна, густая атмосфера, метановые дожди, температура около -180°C.", "temp": "-180°C"},
    "Ио": {"desc": "Спутник Юпитера, множество действующих вулканов, температура от -143°C до -163°C.", "temp": "-143°C до -163°C"}
}

WEATHER_TRUE_FALSE = [
    {"q": "На Венере температура выше, чем на Меркурии.", "a": True},
    {"q": "На Марсе бывают пылевые бури, охватывающие всю планету.", "a": True},
    {"q": "На Юпитере средняя температура выше, чем на Земле.", "a": False},
    {"q": "На Сатурне идут алмазные дожди.", "a": True},
    {"q": "На Меркурии есть атмосфера, похожая на земную.", "a": False},
    {"q": "На Уране и Нептуне очень сильные ветры.", "a": True},
    {"q": "На Земле самая высокая температура среди всех планет.", "a": False},
    {"q": "Плутон официально считается планетой Солнечной системы.", "a": False},
    {"q": "На Титане есть метановые озёра и дожди.", "a": True},
    {"q": "Европа — это спутник Юпитера, покрытый льдом.", "a": True},
    {"q": "Ио — это спутник Марса.", "a": False},
    {"q": "В СССР был запущен первый искусственный спутник Земли.", "a": True},
    {"q": "Валентина Терешкова — первая женщина-космонавт.", "a": True},
    {"q": "На Луне есть атмосфера, пригодная для дыхания.", "a": False},
    {"q": "Гагарин облетел Землю за 108 минут.", "a": True}
]

@bot.message_handler(commands=['start'])
def button_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Интересный факт 🚀"))
    markup.add(types.KeyboardButton("Узнать погоду за бортом"))
    markup.add(types.KeyboardButton("Сыграть в космическую викторину"))
    markup.add(types.KeyboardButton("Моя статистика"))
    markup.add(types.KeyboardButton("Цитата дня"))
    markup.add(types.KeyboardButton("Оставить отзыв"))
    markup.add(types.KeyboardButton("Угадай планету по погоде"))
    markup.add(types.KeyboardButton("Правда или ложь: космическая погода"))
    bot.send_message(message.chat.id, "Привет, космический исследователь! Я расскажу тебе о великих достижениях СССР в космосе. 🌌\n\nВыбери одну из кнопок снизу.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Интересный факт 🚀')
def send_fact(message):
    user_id = str(message.from_user.id)
    if user_id not in sent_facts or len(sent_facts[user_id]) == len(FACTS):
        sent_facts[user_id] = set()
    available = [i for i in range(len(FACTS)) if i not in sent_facts[user_id]]
    idx = random.choice(available)
    sent_facts[user_id].add(idx)
    fact = FACTS[idx]
    gif = GIFS[idx]
    bot.send_animation(message.chat.id, gif)
    bot.send_message(message.chat.id, f"📡 <b>Космический факт СССР:</b>\n\n{fact}", parse_mode="HTML")
    user_stats.setdefault(user_id, {"facts": 0, "quizzes": 0, "max_score": 0, "guess_planet": 0, "true_false": 0})
    user_stats[user_id]["facts"] += 1
    save_stats(user_stats)

@bot.message_handler(func=lambda message: message.text == "Цитата дня")
def send_quote(message):
    quote = random.choice(QUOTES)
    bot.send_message(message.chat.id, f"🛰️ <b>Космическая цитата:</b>\n\n{quote}", parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "Моя статистика")
def my_stats(message):
    user_id = str(message.from_user.id)
    stats = user_stats.get(user_id, {
        "facts": 0,
        "quizzes": 0,
        "max_score": 0,
        "guess_planet": 0,
        "true_false": 0
    })
    bot.send_message(
        message.chat.id,
        f"📊 <b>Твоя статистика:</b>\n"
        f"Фактов просмотрено: {stats.get('facts', 0)}\n"
        f"Викторин сыграно: {stats.get('quizzes', 0)}\n"
        f"Лучший результат в векторине: {stats.get('max_score', 0)} баллов\n"
        f"Игр 'Угадай планету': {stats.get('guess_planet', 0)}\n"
        f"Игр 'Правда или ложь': {stats.get('true_false', 0)}",
        parse_mode="HTML"
    )

@bot.message_handler(func=lambda message: message.text == "Оставить отзыв")
def feedback(message):
    bot.send_message(message.chat.id, "✉️ Напиши свой отзыв или пожелание. Я обязательно его прочитаю!")
    bot.register_next_step_handler(message, save_feedback)
def save_feedback(message):
    username = message.from_user.username or "нет username"
    with open("feedback.txt", "a", encoding="utf-8") as f:
        f.write(f"@{username}: {message.text}\n")
    bot.send_message(message.chat.id, "Спасибо за отзыв! 🚀")

@bot.message_handler(func=lambda message: message.text == "Узнать погоду за бортом")
def ask_city(message):
    bot.send_message(message.chat.id, "Введите название <b>города</b> мимо, которого мы пролетаем", parse_mode="HTML")
    bot.register_next_step_handler(message, send_weather)
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

@bot.message_handler(func=lambda message: message.text == "Угадай планету по погоде")
def guess_planet(message):
    user_id = str(message.from_user.id)
    planet, info = random.choice(list(PLANET_WEATHER.items()))
    user_data[message.from_user.id] = {"planet": planet}
    options = random.sample(list(PLANET_WEATHER.keys()), 3)
    if planet not in options:
        options[0] = planet
    random.shuffle(options)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for opt in options:
        markup.add(types.KeyboardButton(opt))
    markup.add(types.KeyboardButton("Я не знаю"))
    bot.send_message(message.chat.id, f"На какой планете или спутнике такая погода?\n\n{info['desc']}", reply_markup=markup)
    user_stats.setdefault(user_id, {"facts": 0, "quizzes": 0, "max_score": 0, "guess_planet": 0, "true_false": 0})
    if "guess_planet" not in user_stats[user_id]:
        user_stats[user_id]["guess_planet"] = 0
    user_stats[user_id]["guess_planet"] += 1
    save_stats(user_stats)
    bot.register_next_step_handler(message, check_guess_planet)

def check_guess_planet(message):
    planet = user_data.get(message.from_user.id, {}).get("planet")
    if not planet:
        bot.send_message(message.chat.id, "Попробуй начать игру заново.")
        return
    if message.text == planet:
        bot.send_message(message.chat.id, "✅ Верно! Это " + planet + "!")
    else:
        bot.send_message(message.chat.id, f"❌ Неверно! Это была {planet}.")
    button_start(message)

@bot.message_handler(func=lambda message: message.text == "Правда или ложь: космическая погода")
def true_false_weather(message):
    user_id = str(message.from_user.id)
    q = random.choice(WEATHER_TRUE_FALSE)
    user_data[message.from_user.id] = {"tf_answer": q["a"]}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Правда"), types.KeyboardButton("Ложь"))
    markup.add(types.KeyboardButton("Я не знаю"))
    user_stats.setdefault(user_id, {"facts": 0, "quizzes": 0, "max_score": 0, "guess_planet": 0, "true_false": 0})
    if "true_false" not in user_stats[user_id]:
        user_stats[user_id]["true_false"] = 0
    user_stats[user_id]["true_false"] += 1
    save_stats(user_stats)
    bot.send_message(message.chat.id, q["q"], reply_markup=markup)
    bot.register_next_step_handler(message, check_true_false_weather)

def check_true_false_weather(message):
    answer = user_data.get(message.from_user.id, {}).get("tf_answer")
    if answer is None:
        bot.send_message(message.chat.id, "Попробуй начать игру заново.")
        return
    if message.text == "Правда" and answer is True or message.text == "Ложь" and answer is False:
        bot.send_message(message.chat.id, "✅ Верно!")
    elif message.text == "Я не знаю":
        bot.send_message(message.chat.id, "Это был вопрос на размышление! Ответ: " + ("Правда" if answer else "Ложь"))
    else:
        bot.send_message(message.chat.id, "❌ Неверно! Ответ: " + ("Правда" if answer else "Ложь"))
    button_start(message)

@bot.message_handler(func=lambda message: message.text == "Сыграть в космическую викторину")
def choose_tema(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton("Космонавты"), types.KeyboardButton("Спутники"))
    markup.add(types.KeyboardButton("Станции"), types.KeyboardButton("Технологии"))
    bot.send_message(message.chat.id, 'Выберите тему викторины', reply_markup=markup)

def load_questions(topic):
    with open(f"{topic}.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        questions = data["questions"]
        return {
            "easy": questions[:6],
            "medium": questions[6:14],
            "hard": questions[14:]
        }

@bot.message_handler(func=lambda msg: msg.text in ["Космонавты", "Спутники", "Станции", "Технологии"])
def start_quiz(message):
    user_id = str(message.from_user.id)
    topic = message.text.lower()
    user_data[user_id] = {
        "topic": topic,
        "score": 0,
        "questions": load_questions(topic),
        "current_question": None,
        "timer": None
    }
    user_stats.setdefault(user_id, {"facts": 0, "quizzes": 0, "max_score": 0, "guess_planet": 0, "true_false": 0})
    user_stats[user_id]["quizzes"] += 1
    save_stats(user_stats)
    ask_difficulty(message.chat.id, user_id)

def ask_difficulty(chat_id, user_id):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    markup.add(types.KeyboardButton("🟢 Лёгкий"), types.KeyboardButton("🟡 Средний"), types.KeyboardButton("🔴 Сложный"))
    markup.add(types.KeyboardButton("Завершить викторину"))
    questions_left = ""
    for diff, questions in user_data[user_id]["questions"].items():
        if questions:
            emoji = "🟢" if diff == "easy" else "🟡" if diff == "medium" else "🔴"
            questions_left += f"{emoji} {len(questions)} | "
    bot.send_message(chat_id, f"Выбери сложность следующего вопроса:\n(Осталось: {questions_left[:-2]})", reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text in ["🟢 Лёгкий", "🟡 Средний", "🔴 Сложный"])
def set_difficulty(message):
    user_id = str(message.from_user.id)
    if user_id not in user_data:
        return choose_tema(message)
    difficulty_map = {
        "🟢 Лёгкий": "easy",
        "🟡 Средний": "medium",
        "🔴 Сложный": "hard"
    }
    difficulty = difficulty_map[message.text]
    if not user_data[user_id]["questions"][difficulty]:
        bot.send_message(message.chat.id, f"Вопросы уровня {message.text} закончились!")
        return ask_difficulty(message.chat.id, user_id)
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
    options = question["options"]
    random.shuffle(options)
    markup = types.InlineKeyboardMarkup()
    row = []
    for i, option in enumerate(options):
        callback_data = f"ans_{i}_{option}"
        row.append(types.InlineKeyboardButton(option, callback_data=callback_data))
        if len(row) == 2:
            markup.row(*row)
            row = []
    if row:
        markup.row(*row)
    diff_emoji = "🟢" if difficulty == "easy" else "🟡" if difficulty == "medium" else "🔴"
    timer_seconds = 30
    msg = bot.send_message(
        chat_id,
        f"{diff_emoji} Вопрос ({difficulty.capitalize()}):\n\n{question['question']}\n\n⏳ Осталось: {timer_seconds} сек.",
        reply_markup=markup
    )
    user_data[user_id]["question_msg_id"] = msg.message_id
    user_data[user_id]["timer_seconds"] = timer_seconds
    user_data[user_id]["timer_cancel"] = False
    user_data[user_id]["timer_start"] = time.time()

    def update_timer():
        for sec in range(timer_seconds - 1, 0, -1):
            if user_id not in user_data or user_data[user_id].get("timer_cancel"):
                break
            next_tick = user_data[user_id]["timer_start"] + (timer_seconds - sec)
            sleep_time = max(0, next_tick - time.time())
            time.sleep(sleep_time)
            if user_id not in user_data or user_data[user_id].get("timer_cancel"):
                break
            try:
                bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=msg.message_id,
                    text=f"{diff_emoji} Вопрос ({difficulty.capitalize()}):\n\n{question['question']}\n\n⏳ Осталось: {sec} сек.",
                    reply_markup=markup
                )
            except:
                pass
            user_data[user_id]["timer_seconds"] = sec
    threading.Thread(target=update_timer, daemon=True).start()
    if user_data[user_id].get("timer"):
        user_data[user_id]["timer"].cancel()
    timer = threading.Timer(timer_seconds, timeout_question, args=[chat_id, user_id])
    user_data[user_id]["timer"] = timer
    timer.start()

def timeout_question(chat_id, user_id):
    if user_id in user_data and not user_data[user_id].get("timer_cancel"):
        user_data[user_id]["timer_cancel"] = True
        question = user_data[user_id]["current_question"]["question"]
        bot.send_message(chat_id, f"⏰ Время вышло! Правильный ответ: {question['answer']}\n{question['explanation']}")
        ask_difficulty(chat_id, user_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith("ans_"))
def handle_answer(call):
    user_id = str(call.from_user.id)
    if user_id not in user_data:
        return
    user_data[user_id]["timer_cancel"] = True
    if user_data[user_id].get("timer"):
        user_data[user_id]["timer"].cancel()
    parts = call.data.split("_")
    selected_idx = int(parts[1])
    selected_text = "_".join(parts[2:])
    question = user_data[user_id]["current_question"]["question"]
    difficulty = user_data[user_id]["current_question"]["difficulty"]
    if selected_text == question["answer"]:
        points = {"easy": 1, "medium": 3, "hard": 5}[difficulty]
        user_data[user_id]["score"] += points
        response = f"✅ Верно! +{points} баллов"
    else:
        response = f"❌ Неверно! Правильный ответ: {question['answer']}"
    try:
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"{call.message.text}\n\n{response}",
            reply_markup=None
        )
    except:
        pass
    bot.send_message(call.message.chat.id, f"📚 Пояснение:\n{question['explanation']}\n\nТвой счет: {user_data[user_id]['score']}")
    total_questions_left = sum(len(q) for q in user_data[user_id]["questions"].values())
    if total_questions_left == 0:
        finish_quiz(call.message.chat.id, user_id)
    else:
        ask_difficulty(call.message.chat.id, user_id)

@bot.message_handler(func=lambda msg: msg.text == "Завершить викторину")
def quit_quiz(message):
    user_id = str(message.from_user.id)
    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сейчас викторина не запущена. Нажмите 'Сыграть в космическую викторину', чтобы начать!")
        return
    user_data[user_id]["timer_cancel"] = True
    if user_data[user_id].get("timer"):
        user_data[user_id]["timer"].cancel()
    finish_quiz(message.chat.id, user_id, manual=True)

def finish_quiz(chat_id, user_id, manual=False):
    score = user_data[user_id]["score"]
    topic = user_data[user_id]["topic"]
    if score >= 30:
        rank = "👨‍🚀 Генерал космических войск!"
    elif score >= 20:
        rank = "🛰️ Главный конструктор!"
    elif score >= 10:
        rank = "🚀 Космический инженер!"
    else:
        rank = "🌍 Начинающий исследователь!"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Интересный факт 🚀"))
    markup.add(types.KeyboardButton("Узнать погоду за бортом"))
    markup.add(types.KeyboardButton("Сыграть в космическую викторину"))
    markup.add(types.KeyboardButton("Моя статистика"))
    markup.add(types.KeyboardButton("Цитата дня"))
    markup.add(types.KeyboardButton("Оставить отзыв"))
    markup.add(types.KeyboardButton("Угадай планету по погоде"))
    markup.add(types.KeyboardButton("Правда или ложь: космическая погода"))
    if manual:
        bot.send_message(chat_id,
            f"🏁 Викторина завершена по вашему запросу!\n\n"
            f"Тема: {topic.capitalize()}\n"
            f"Набрано баллов: {score}\n"
            f"Твое звание: {rank}",reply_markup=markup
        )
    else:
        bot.send_message(chat_id,
            f"🏆 Викторина завершена!\n\n"
            f"Тема: {topic.capitalize()}\n"
            f"Набрано баллов: {score}\n"
            f"Твое звание: {rank}",reply_markup=markup
        )
    user_stats.setdefault(user_id, {"facts": 0, "quizzes": 0, "max_score": 0, "guess_planet": 0, "true_false": 0})
    if score > user_stats[user_id]["max_score"]:
        user_stats[user_id]["max_score"] = score
        save_stats(user_stats)
    if user_id in user_data:
        del user_data[user_id]

bot.polling(none_stop=True)
