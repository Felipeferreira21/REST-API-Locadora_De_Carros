from flask_restful import Resource, reqparse
from flask import Flask, jsonify, request
from models.carro import *
from bd import *

class Carros(Resource):
    def get(self):
        return {"carros": carros}


class Carro(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('ano')
    atributos.add_argument('marca')
    atributos.add_argument('diaria')
    atributos.add_argument('situacao')

    def find_carro(modelo):
        carros_encontrados = [carro for carro in carros if carro['modelo'] == modelo]
        return carros_encontrados


    def get(self, modelo):
        carro = Carro.find_carro(modelo)
        if carro:
            return carro
        return {"message": "Não temos esse modelo disponivel"}, 404
    
     
    def post(self, modelo):
        dados = Carro.atributos.parse_args()
        carro_objeto = CarroModel(modelo, **dados)
        novo_carro = carro_objeto.json()
        carros.append(novo_carro)
        return novo_carro, 201


class Add_edit_delet(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('marca')
    atributos.add_argument('diaria')
    atributos.add_argument('situacao')

    def find_carro(modelo, ano):
        for carro in carros:
            if carro['modelo'] == modelo and carro['ano'] == ano:
                return carro
        return False


    def put(self, modelo, ano):
        dados = Add_edit_delet.atributos.parse_args()
        carro_objeto = CarroModel(modelo, ano, **dados)
        novo_carro = carro_objeto.json()
        carro = Add_edit_delet.find_carro(modelo, ano)
        if carro:
            carro.update(novo_carro)
            return novo_carro, 200
        carros.append(novo_carro)
        return novo_carro, 201


    def delete(self, modelo, ano):
        global carros
        carros = [carro for carro in carros if (carro['modelo']) != modelo or (carro['ano']) != ano]
        return carros, 200


class Clientes(Resource):
    def get(self):
        return {"carros": carros}