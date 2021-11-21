from flask import Flask, request

app = Flask(__name__)


@app.route('/phones/create/')
def contact_create():
    import sqlite3

    phone_value = request.args['phone']
    contact_name = request.args['name']

    con = sqlite3.connect('users.db')
    cur = con.cursor()

    sql = f'''
    INSERT INTO Phones (phoneValue, contactName) VALUES ('{phone_value}', '{contact_name}')
    '''

    cur.execute(sql)
    con.commit()
    con.close()

    return 'contact_create'


@app.route('/phones/read/')
def sql_read():
    import sqlite3

    con = sqlite3.connect('users.db')
    cur = con.cursor()

    sql = f'''
            SELECT * FROM Phones
    '''

    cur.execute(sql)
    result = cur.fetchall()
    con.commit()
    con.close()

    return str(result)


@app.route('/phones/update/')
def phones_update():
    import sqlite3

    phone_value = request.args['phone']
    contact_name = request.args['name']
    phone_id = request.args['id']

    con = sqlite3.connect('users.db')
    cur = con.cursor()

    sql = f'''
    UPDATE Phones
    SET phoneValue = '{phone_value}', contactName = '{contact_name}'
    WHERE phoneID = {phone_id};
    '''

    cur.execute(sql)
    con.commit()
    con.close()

    return 'contact_update'


@app.route('/phones/delete/')
def contact_delete():
    import sqlite3

    phone_id = request.args['id']
    con = sqlite3.connect('users.db')
    cur = con.cursor()

    sql = f'''
    DELETE FROM Phones
    WHERE phoneID = {phone_id};
    '''

    cur.execute(sql)
    con.commit()
    con.close()

    return 'contact_delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
