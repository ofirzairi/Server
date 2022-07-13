from flask import Blueprint, render_template
import mysql.connector
from flask import request, redirect
from flask import jsonify
import requests



assignment_4 = Blueprint('assignment_4', __name__,
                         static_folder='static',
                         template_folder='templates')


@assignment_4.route('/assignment_4')
def assignment4_func():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', users=users_list)



@assignment_4.route('/insert', methods=['POST'])
def insert():
    email = request.form['userName']
    password = request.form['password']
    name = request.form['Name']
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    for user in users_list:
        if email == user.email:
            return render_template('assignment_4.html',
                                    message1='It seems this user is already exists',
                                    users=users_list)

    if name == ' ':
                query_1 = 'select * from users'
                users_list1 = interact_db(query=query_1, query_type='fetch')
                return render_template('assignment_4.html', users=users_list1, message1='Enter your User Name')
    else:
                query = "INSERT INTO users(email,password,name) VALUES ('%s','%s','%s')" % (email, password, name)
                interact_db(query=query, query_type='commit')
                query_1 = 'select * from users'
                users_list1 = interact_db(query=query_1, query_type='fetch')
                return render_template('assignment_4.html',
                                        message1='You are now officially a Yogi',
                                        users=users_list1)



@assignment_4.route('/update', methods=['POST'])
def update():
    email = request.form['userName']
    password = request.form['password']
    name = request.form['Name']
    if password != "" and name != "":
        query = "UPDATE users SET password='%s',name='%s' WHERE email='%s' " % (password, name, email)
        interact_db(query=query, query_type='commit')
        query_1 = 'select * from users'
        users_list = interact_db(query=query_1, query_type='fetch')
        return render_template('assignment_4.html',
                                message2='Your password and name were successfully updated',
                                users=users_list)
    elif name != "" and password == "":
        query = "UPDATE users SET name='%s' WHERE email='%s' " % (name, email)
        interact_db(query=query, query_type='commit')
        query_1 = 'select * from users'
        users_list = interact_db(query=query_1, query_type='fetch')
        return render_template('assignment_4.html',
                               message2='Your name was successfully updated',
                               users=users_list)
    elif password != "" and name == "":
        query = "UPDATE users SET password='%s' WHERE email='%s' " % (password, email)
        interact_db(query=query, query_type='commit')
        query_1 = 'select * from users'
        users_list = interact_db(query=query_1, query_type='fetch')
        return render_template('assignment_4.html',
                               message2='Your password was successfully updated',
                               users=users_list)
    else:
        query_1 = 'select * from users'
        users_list = interact_db(query=query_1, query_type='fetch')
        return render_template('assignment_4.html',
                               message2='please fill in the required fields!',
                               users=users_list)

@assignment_4.route('/delete', methods=['POST'])
def delete():
    email = request.form['userName']
    query = "DELETE FROM users WHERE email='%s';" % email
    interact_db(query=query, query_type='commit')
    query_1 = 'select * from users'
    users_list = interact_db(query=query_1, query_type='fetch')
    return render_template('assignment_4.html',
                            message5='User deleted',
                            users=users_list)



def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='schema_assignment4')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)


    if query_type == 'commit':
        connection.commit()
        return_value = True


    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment_4.route('/assignment_4/users')
def users_response():
    query = 'select * from users'
    query_list = interact_db(query, query_type='fetch')
    return jsonify(query_list)

@assignment_4.route('/assignment_4/outer_source')
def outer_source():
    return render_template('outer_source.html')



@assignment_4.route('/assignment_4/outer_source/fetch_backend')
def backend():
    user_id = request.args['user_id']
    res = requests.get(f"https://reqres.in/api/users/{user_id}")
    return render_template('outer_source.html', request_data=res.json()['data'])




@assignment_4.route('/assignment4/restapi_users/', defaults={'user_id': -1})
@assignment_4.route('/assignment4/restapi_users/<user_id>')
def get_user(user_id):
    if user_id == -1:
        query = f'SELECT * FROM users'
        users_list = interact_db(query, query_type='fetch')
        return_list = []
        user = users_list[2]
        user_dict = {
                'name': user.name,
                'email': user.email
            }

        return jsonify(user_dict)

    else:
        query = f'SELECT * FROM users WHERE id={user_id}'
        users_list = interact_db(query, query_type='fetch')
        if len(users_list) == 0:
            return_dict = {
                'message': 'user was not found, try again.'
            }
        else:
            user = users_list[0]
            return_dict = {
                'name': user.name,
                'email': user.email
            }
    return jsonify(return_dict)


















