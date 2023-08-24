from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Welcome All"
    
# GitAction WorkFlow is successfully doing it;s job!!


#app.run(port=5008, debug=True)