# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get("button_discord")
    email= request.form.get("email")
    oneri= request.form.get("text")
    with open("oneriler.txt", "w") as f:
        f.write("Email: {}\n".format(email))
        f.write("Öneri: {}\n".format(oneri))
    return render_template('index.html', button_python=button_python, button_discord=button_discord, email=email, oneri=oneri)


if __name__ == "__main__":
    app.run(debug=True)
