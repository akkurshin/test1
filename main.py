from flask import Flask, session, request, redirect, url_for, render_template


app = Flask(__name__)  



def index():
    if request.method == 'GET':
        a = request.args.get('name')
        print(a)
        return '''<!DOCTYPE html>
            <html>
            <head>
            <title>Анкета</title>
            </head>
            <body>
            <form method="get" action="/">
            <p><h2>Заполните анкету:</h2>
            <p><b>Ваше имя:</b> <input type="text" name="name"> </p>     
                <p><b>Ваша фамилия:</b> <input type="text" name="surname"></p>     
            <p><b>Ваш возраст:</b> <input type="number" name="age"></p>     
            
            <p><b>Выберите курсы, которые Вас интересуют:</b></p>
            <p><input type="checkbox" name="a" value="s">Scratch</p>
            <p><input type="checkbox" name="a" value="g">Gamedesign</p>
            <p><input type="checkbox" name="a" value="ps">Python Start</p>
            <p><input type="checkbox" name="a" value="pp">Python Pro</p>  
            <p><b>Дополнительный комментарий:</b> <textarea name="comment">  </textarea></p>
                <p><input type="submit" value="Отправить"></p>
            </form>
            </body>
            </html>'''
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        age = request.form.get('age')
        course = request.form.get('a')
        comment = request.form.get('comment')
        print(name, surname, age, course, comment)

        return '<h1>форма отправлена!</h1>'
app.add_url_rule('/', 'index', index, methods=['post', 'get']) # правило для '/index' 
 
if __name__ == "__main__":
   app.run()
