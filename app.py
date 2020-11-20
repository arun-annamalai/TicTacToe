from flask import render_template
from server import app

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)