from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    user = { 'username':}
    user = {'usernaame':'Dhiraj'}
    posts = [
        {
            'author':{'username':'daneil'},
            'body':'Beautful day in Srilanka!'
            },
        {
            'author':{'username':'Amar'},
            'body':'Tiger hey movie was so cool!'
            }
        ]
    
    return render_template('index.html', usser=user, posts=posts)


if __name__ == '__main__':
    app.run
                           
