from flask import Flask

app = Flask(__name__)
import routes.square, routes.lazy_developer, routes.greedy_monkey