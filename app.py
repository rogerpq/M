from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'The Best Of Userbot RepThon'


if __init__ == "__main__":
  app.run
