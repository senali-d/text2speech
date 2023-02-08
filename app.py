from flask import Flask, render_template, request

from main import text_to_speech
 
app = Flask(__name__)
 
@app.route("/",  methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    text = request.form['speech']
    text_to_speech(text)
    return render_template('index.html')
  else:
    return render_template('index.html')
 
  if __name__ == "__main__":
    app.run()