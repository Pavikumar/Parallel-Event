import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
        return 'It\'s Parallelevent!!'

@app.route('/foo/')
def fello():
        return 'Foo Parallelevent!!'

@app.route('/bar/')
def bello():
        return 'Bar Parallelevent!!'
    
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
