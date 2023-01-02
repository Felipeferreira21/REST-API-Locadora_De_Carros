
from flask import Flask
from flask_restful import Api
from resources.carro import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Carros, '/carros')
api.add_resource(Carro, '/carros/<string:modelo>')
api.add_resource(Clientes, '/carros/<string:nome>')
api.add_resource(Add_edit_delet, '/carros/<string:modelo>/<int:ano>')

if __name__ == '__main__':
    app.run(debug=True)