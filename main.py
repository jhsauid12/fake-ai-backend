from flask import Flask, request, jsonify
import random

app = Flask(__name__)

def fake_thought_response(msg):
    ideas = [
        "��� ���������� ������. ��������, �� ������ � {}. � �� �����������, ��� {}.",
        "���... �����, ��� {}. ���� ��� ������� �� ������ ��������.",
        "��� ���������� ������ ������������, ��� {}.",
        "����� ���������� ���: {}. ���� ������ ����� ���� ������.",
    ]
    topic = extract_topic(msg)
    fill = f"��� ������� � '{topic}'" if topic else "�� ������� �������, ��� �������"
    return random.choice(ideas).format(topic or "����", fill)

def extract_topic(msg):
    keywords = {
        "������": "���������� �������",
        "��": "����������� � �������� ���������",
        "�����": "����������",
        "�����": "����������������",
        "������": "�������� � ���������",
        "������": "����������� � ������� �������� ������",
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

    if "������" in msg:
        response = "������ +23�C � ��������. �������� ���� ��� �����������."
    elif "��� ����" in msg or "��� ��" in msg:
        response = "� ������������ ���������. ����� �������� �� ����� �������."
    else:
        response = fake_thought_response(msg)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()
