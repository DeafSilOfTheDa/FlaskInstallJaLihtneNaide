from flask import Flask
import json
from flask import request
from flask import render_template
app = Flask(__name__)




@app.route("/")
def index():
    return render_template('index.html')

@app.route('/kasutajad', methods=['POST'])
def kasutajad():
    kasutajad_vali =request.form.get("kasutajad")




    print(kasutajad_vali)
    return ""










#@app.route("/") #postitab kasutajad
def hello():
    data = json.dumps(
        {"kasutajad":
             [
                 {"kasutaja_nimi1": "Kellegi nimi "},
                 {"kasutaja_nimi": "Teise kasutaja nimi"},
                 {"kasutaja_nimi": "kellegi kolmanda nimi"}
             ]
        }
    )

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='aplication/json'
    )
    return response



@app.route("/post_example", methods=["POST"])
def hello_post_example():
    users = json.loads(request.form.get("kasutajad"))
    users["kasutajad"] #küsib dictionarid



    print("Server1 ", request.form.get("kasutajad"))
    return ""