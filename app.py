
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "API Sự Kiện Hôm Nay hoạt động!"

if __name__ == '__main__':
    app.run()
