from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Xin chào từ Flask! Đây là API cà phê Sự Kiện Hôm Nay!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
