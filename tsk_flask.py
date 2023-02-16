from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Регистрация претендента</title>
                          </head>
                          <body>
                            <div>
                                <form class="login_form" method="post">
                                    <h1>Анкета претендента</h1>
                                    <h3>на участие в миссии</h3>
                                    <input class="surname" placeholder="Введите вашу фамилию" name="surname">
                                    <input class="firstname" placeholder="Введите ваше имя" name="firstname">
                                    <p></p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <p></p>
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Общее образование</option>
                                          <option>Профессиональное образование</option>
                                          <option>Дополнительное образование</option>
                                          <option>Профессиональное обучение</option>
                                        </select>
                                     </div>
                                    <p></p>
                                    <div class="form-group">
                                        <label for="form-check">Какие у вас профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="engineer-builder" value="engineer-builder" checked>
                                          <label class="form-check-label" for="engineer-builder">
                                            Инженер-cтроитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="engineer-researcher" value="engineer-researcher" checked>
                                          <label class="form-check-label" for="engineer-researcher">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="doctor" value="doctor" checked>
                                          <label class="form-check-label" for="doctor">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="pilot" value="pilot" checked>
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="lifesystem" value="lifesystem" checked>
                                          <label class="form-check-label" for="lifesystem">
                                            Специалист по жизнеобеспечению
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="ekzobio" value="ekzobio" checked>
                                          <label class="form-check-label" for="ekzobio">
                                            Экзобиолог
                                          </label>
                                        </div>
                                    <p></p>
                                    <div class="form-group">
                                        <label for="form-check">Укажите ваш пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female" checked>
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <p></p>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <p></p>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите участвовать в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <p></p>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                    </div>
                                </form>
                            </div>
                            </body>
                          </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
