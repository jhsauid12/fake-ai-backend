from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешаем запросы с других доменов (например, с Netlify)

# Корневой маршрут для проверки (устраняет 404 от GET / и OPTIONS /)
@app.route("/", methods=["GET"])
def index():
    return "Backend is running", 200

# Основной маршрут API
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()

    # Проверка на наличие поля "message"
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data["message"]
    print("Сообщение от пользователя:", user_message)

    # Здесь можно вставить логику обращения к ИИ
    response = "ИИ: Печатает..."

    return jsonify({"response": response})

# Запуск сервера локально (Render сам вызывает gunicorn, поэтому этот блок не используется)
if __name__ == "__main__":
    app.run(debug=True)
