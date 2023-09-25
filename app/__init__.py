from flask import Flask, request

app = Flask(__name__)

from resources.trainers import routes

from resources.pokemon import routes