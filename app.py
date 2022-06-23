from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from datetime import timedelta

app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)


user_dict = {'Amitallgood2@gmail.com': ['5678', 'Amit Ganzi'],
             'Nadoovi@gmail.com': ['3491', 'Nadav Moss'],
             'yuvi85@gmail.com': ['1905', 'Yuval Zairi'],
             'Yooli34@gmail.com': ['3918', 'Yael Hakim'],
             'guyZO@gmail.com': ['2718', 'Guy Pines']}

teachers_dict = {'Ashtanga': ['Maya Gross', 'Roni Anice', 'Kathryn Budig'],
                 'Vinyasa': ['Josephine Jacob', 'Sara Clark', 'Rina chen'],
                 'Hatha': ['Dana Arnold','Ben Cohen','Roni Duani'],
                 'Iyengar': ['Amit Tene', 'Inbal Baba', 'Suzana Crazy'],
                 'Bikram': ['Adi Motin', 'Tomer Doss', 'Beri Tzakala']}



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('HomePage.html')


@app.route('/contact/')
def contact():
    return render_template('Contact.html')


@app.route('/assignment3_1')
def assignment3_1():
    user_name = ''
    yoga_types = ['Vinyasa Yoga', 'Hatha Yoga', 'Ashtanga Yoga','Iyengar Yoga', 'Bikram Yoga']
    return render_template('assignment3_1.html', user_name=user_name, yoga_types=yoga_types)


@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2():
    connected = False
    if request.method == 'POST':
        username = request.form['userName']
        Nickname = request.form['Name']
        password = request.form['password']
        if username in user_dict:
            pas_in_dict = user_dict[username][0]
            name_in_dict = user_dict[username][1]
            if pas_in_dict == password and name_in_dict == Nickname:
                session['userName'] = Nickname
                session['logedin'] = True
                connected = True
                return render_template('assignment3_2.html', message1 ='Welcome back', userName=Nickname)
            else:
                return render_template('assignment3_2.html',
                                       message2='oops, this user name is unavailable. Please try something else')
        else:
                user_dict[username] = [password, Nickname]
                print(user_dict)
                session['userName'] = Nickname
                session['logedin'] = True
                return render_template('assignment3_2.html', message3='Welcome to our Studio', userName=Nickname)

    elif 'yoga_type' in request.args:
        yoga_type = request.args['yoga_type']
        if yoga_type is '':
            return render_template('assignment3_2.html', teachers_dict=teachers_dict)
        elif yoga_type in teachers_dict:
            return render_template('assignment3_2.html', yoga_type=yoga_type,
                                                        teacher_1=teachers_dict[yoga_type][0],
                                                        teacher_2 =teachers_dict[yoga_type][1],
                                                        teacher_3=teachers_dict[yoga_type][2])
        else:
            return render_template('assignment3_2.html', message4='We do not teach this type of yoga in our studio')

    elif connected:
        return render_template('assignment3_2.html', message1='Welcome back')

    else:
        return render_template('assignment3_2.html')


@app.route('/endSession')
def logout_func():
    session['logedin'] = False
    connected = False
    session.clear()
    return redirect(url_for('assignment3_2'))


@app.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))



if __name__ == '__main__':
    app.run(debug=True)







