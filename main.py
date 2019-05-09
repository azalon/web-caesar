from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """ 


<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      
      <form name="rotate" method='post'>
          <label for="rotate_num" > Rotate by:</label>
          <input id= "rotate_num" type="text" name="rot" value="0"/>
          <textarea name="text">
            {0}
          </textarea>
          <input type="submit" value="Submit query"/>
         

      </form>
    </body>
</html>

"""

@app.route('/', methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    text = rotate_string(text, rot)

    return form.format(text) 

@app.route("/")
def index():
    return form.format("")
    
app.run()