from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o formulário
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    if name:
        message = f"Olá, {name}! Bem-vindo ao app Flask!"
    else:
        message = "Olá! Por favor, insira seu nome."
    return render_template('greet.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
