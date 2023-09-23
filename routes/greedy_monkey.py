import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)


@app.route('/greedymonkey', methods=['POST'])
def greedymonkey():
    data = json.loads(request.data)
    w = data["w"]
    v = data["v"]
    f = data["f"]

    max_value = max_monkey_value(w, v, f)

    return str(max_value)


def max_monkey_value_memo(w, v, f, n, memo):
    if n == 0 or w == 0 or v == 0:
        return 0

    if memo[w][v][n] != -1:
        return memo[w][v][n]

    weight, volume, value = f[n - 1]

    if weight > w or volume > v:
        result = max_monkey_value_memo(w, v, f, n - 1, memo)
    else:
        include_fruit = value + max_monkey_value_memo(w - weight, v - volume, f, n - 1, memo)
        exclude_fruit = max_monkey_value_memo(w, v, f, n - 1, memo)
        result = max(include_fruit, exclude_fruit)

    memo[w][v][n] = result
    return result

def max_monkey_value(w, v, f):
    n = len(f)
    memo = [[[-1 for _ in range(n + 1)] for _ in range(v + 1)] for _ in range(w + 1)]
    
    return max_monkey_value_memo(w, v, f, n, memo)