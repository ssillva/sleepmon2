#!/usr/bin/python
# -*- coding: utf-8 -*-
#Sandro
import sqlite3

class ConexaoBD(object):
    #inicializando o Banco de dados
    def __init__( self, bdName ):
        try:
            #dfefinindo atributo conexao
            self.conexao = sqlite3.connect(bdName)
            #definindo atributo direcionador
            self.direcionador = self.conexao.cursor()
            print "Conexão com BD estabelecida"
        except sqlite3.Error:
            #mensagem de erro caso não abra o BD
            print("Erro na conexao do banco de dados!")
            return False

#confirmar e salvar os dados no Banco de dados
    def commit_banco(self):
        if (self.conexao):
            self.conexao.commit()

#Fechando a conexão com Banco de dados
    def fechar_banco(self):
        try:
            if self.conexao:
                self.conexao.close()
                print ("Conexão com BD encerrada!")
        except:
            print ("Não há conexao com BD")
#criando schema
    def cria_schema(self, sensor):
        try:
            self.direcionador.execute("CREATE TABLE %s(Data DATE NOT NULL, Temperatura FLOAT NOT NUL);" %sensor)
        except sqlite3.Error:
            print "Erro na conexao com BD"