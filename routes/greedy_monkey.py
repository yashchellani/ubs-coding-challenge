import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)


@app.route('/greedymonkey', methods=['POST'])
def greedymonkey():
    # Parse the JSON input
    data = json.loads(request.data)
    w = data["w"]  # Maximum weight the monkey can lift
    v = data["v"]  # Volume of the basket
    f = data["f"]  # List of fruits with weight, volume, and value

    # Initialize a 2D table to store the maximum value at each state (i, j)
    dp = [[0] * (v + 1) for _ in range(w + 1)]

    # Fill in the table using dynamic programming
    for fruit in f:
        weight, volume, value = fruit
        for i in range(w, weight - 1, -1):
            for j in range(v, volume - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - weight][j - volume] + value)

    # The maximum value is stored in dp[w][v]
    max_value = dp[w][v]

    # Return the maximum value as a string
    return str(max_value)