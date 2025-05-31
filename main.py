from flask import Flask, request, jsonify
import random

app = Flask(__name__)

def fake_thought_response(msg):
    ideas = [
        "Это интересный вопрос. Возможно, он связан с {}. Я бы предположил, что {}.",
        "Хмм... Думаю, что {}. Хотя это зависит от многих факторов.",
        "Мой внутренний анализ подсказывает, что {}.",
        "Можно рассуждать так: {}. Хотя истина может быть глубже.",
    ]
    topic = extract_topic(msg)
    fill = f"это связано с '{topic}'" if topic else "всё гораздо сложнее, чем кажется"
    return random.choice(ideas).format(topic or "этим", fill)

def extract_topic(msg):
    keywords = {
        "погода": "изменением климата",
        "ИИ": "нейросетями и машинным обучением",
        "жизнь": "философией",
        "время": "относительностью",
        "любовь": "эмоциями и биохимией",
        "космос": "астрономией и теорией большого взрыва",
    }
    for k, v in keywords.items():
        if k in msg.lower():
            return v
    return None

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")
    response = ""

    if "погода" in msg:
        response = "Сейчас +23°C и солнечно. Отличный день для размышлений."
    elif "как дела" in msg or "как ты" in msg:
        response = "Я функционирую стабильно. Готов отвечать на любые вопросы."
    else:
        response = fake_thought_response(msg)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()
