from flask import Flask, request, jsonify

app = Flask(__name__)

# Путь для главной страницы
@app.route('/')
def index():
    return "Сервер работает. Переходите на страницу регистрации."

# Путь для обработки формы регистрации
@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    
    if email:
        # Выводим email в консоль
        print(f"Получен email: {email}")
        
        # Сохранение электронной почты в файл (опционально)
        with open('emails.txt', 'a') as file:
            file.write(f'{email}\n')
        
        return jsonify({'message': 'Регистрация успешна'}), 200
    else:
        return jsonify({'message': 'Ошибка: Необходимо указать email'}), 400

if __name__ == '__main__':
    app.run(debug=True)
