from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)


def get_advice(feeling):
    feeling = feeling.lower()  
    responses = {
        'triste': [
            "Sinto muito que você esteja triste. Lembre-se de que isso também vai passar. Cuide de si mesmo!",
            "Às vezes, é normal sentir-se triste. Tente focar em coisas que te fazem feliz."
        ],
        'entediado': [
            "Que tal tentar algo novo para se distrair? Uma boa leitura pode ser revigorante!",
            "Se estiver entediado, que tal experimentar uma nova atividade? Pode ser divertido!"
        ],
        'alegre': [
            "Que bom que você está alegre! Continue assim e espalhe sua felicidade por aí!",
            "Fico feliz que esteja alegre! Aproveite cada momento!"
        ],
        'feliz': [
            "Que maravilhoso! A felicidade é uma sensação incrível. Continue aproveitando esse momento!",
            "A felicidade está em coisas simples. Que ela dure para sempre!"
        ],
        'desanimado': [
            "Todos nós passamos por momentos de desânimo. Respire fundo e tente dar o primeiro passo!",
            "O desânimo é só uma fase. Tenha fé, as coisas vão melhorar!"
        ],
        'com raiva': [
            "A raiva pode ser difícil de controlar, mas respire fundo e tente se acalmar. Vai passar!",
            "Quando você sentir raiva, tente dar um tempo para si mesmo e refletir sobre o que causou essa sensação."
        ],
        'bravo': [
            "Entendo que você esteja bravo, mas procure um espaço tranquilo para relaxar e refletir.",
            "A raiva pode ser uma emoção forte, mas lembre-se de que você tem o controle sobre suas ações."
        ],
        'calmo': [
            "Que bom que você está calmo! Aproveite esse momento de paz.",
            "A tranquilidade é algo maravilhosa. Que ela continue com você."
        ],
        'tranquilo': [
            "Fico feliz que esteja tranquilo. Aproveite esse momento de serenidade!",
            "A paz interior é um dos maiores presentes que podemos ter. Continue assim!"
        ],
        'cansado': [
            "O cansaço é natural, mas lembre-se de que um bom descanso vai revigorar suas energias!",
            "Quando estiver cansado, tire um tempo para descansar. Seu corpo e mente agradecem!"
        ]
    }
    for key in responses:
        if key in feeling:
            return random.choice(responses[key])
    return "Desculpe, não entendi exatamente o que você está sentindo. Tente algo diferente."

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    feeling = request.form["feeling"]
    advice = get_advice(feeling)
    return jsonify({"response": advice})

if __name__ == "__main__":
    app.run(debug=True)


