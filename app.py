from flask import Flask

app=Flask(__name__)

#POST used to receive data
#GET used to send data back to browser.

# POST/store  data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

#GET /store/<string:name>
@app.rout('/store/<string:name>')
def get_store(name):
    pass

#GET /store
@app.route('/store')
def get_store():
    pass

#POST /store/<string:name>/item{name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store(name):
    pass

#GET/store/<string:name>/item{name:,price:}
@app.route('/store/<string:name>/item', methods=['GET'])
def get_store(name):
    pass


app.run()