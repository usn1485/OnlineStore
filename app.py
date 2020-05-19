from flask import Flask

app=Flask(__name__)

#POST used to receive data
#GET used to send data back to browser.

# POST/store  data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

app.run()