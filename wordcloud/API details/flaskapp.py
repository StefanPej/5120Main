import mysql.connector
from flask import Flask, request, g
from flask_restful import Api, Resource, reqparse
import json

DB_ENDPOINT = "tp22main.ckwpvpzfxlw0.us-west-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASS = "12345678"
DB = "main"

db = mysql.connector.connect(
    host=DB_ENDPOINT,
    user=DB_USER,
    password=DB_PASS,
    database=DB
)

cursor = db.cursor()

app = Flask(__name__)
api = Api(app)


class Users(Resource):

    def get(self):

        cursor.execute("SELECT * FROM wordcloud")
        data = cursor.fetchall()
        clean = []

        for row in data:
            vocab = json.loads(row[3])
            wordcounts = []
            for k, v in vocab.items():
                wordcounts.append({"word": k, "count": v})
            clean.append({"source": row[1], "handle": row[2], "wordcounts": wordcounts})
        return clean, 200


class VocabNoNames(Resource):

    def get(self):

        cursor.execute("SELECT * FROM wordcloud WHERE wc_id = 2")
        data = cursor.fetchall()
        clean = []

        for row in data:
            vocab = json.loads(row[3])
            wordcounts = []
            for k, v in vocab.items():
                wordcounts.append({"word": k, "count": v})
            clean.append({"source": row[1], "handle": row[2], "wordcounts": wordcounts})
        return clean, 200

api.add_resource(Users, "/users")
api.add_resource(VocabNoNames, "/vocabs2")

if __name__ == '__main__':
    app.run()