from flask import Flask, render_template, request
from sense_hat import SenseHat 
from presents import Gift

sense = SenseHat()

app = Flask(__name__)

gift = Gift([], [], [])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def action():
    user_input = request.form['box']
    if user_input == "pink":
        gift.box = "pink"
        print("the giftbox is pink")
    elif user_input == "blue":
        gift.box = "blue"
        print("the giftbox is blue")
    elif user_input == "green":
        gift.box = "green"
        print("the giftbox is green")
    elif user_input == "yellow":
        gift.box = "yellow"
        print("the giftbox is yellow")
       
    return render_template('index.html')

def action():
    user_input = request.form['ribbon']
    if user_input == "pink":
        gift.box = "pink"
        print("the ribbon is pink")
    elif user_input == "blue":
       gift.box = "blue"
       print("the ribbon is blue")
    elif user_input == "green":
        gift.box = "green"
        print("the ribbon is green")
    elif user_input == "yellow":
        gift.box = "yellow"
        print("the ribbon is yellow")
       
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

