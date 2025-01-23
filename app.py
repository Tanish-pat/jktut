from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Jenkins CI/CD!"

def stop_server():
    # This function stops the Flask server after 5 seconds
    os._exit(0)

if __name__ == "__main__":
    # Start the timer to stop the server after 5 seconds
    timer = threading.Timer(5.0, stop_server)
    timer.start()

    app.run(host="0.0.0.0", port=5000)
