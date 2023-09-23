import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)


@app.route('/lazy-developer', methods=['POST'])
def evaluate_lazy_dev():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    input_value = data
    result = getNextProbableWords(input_value["classes"], input_value["statements"])
    logging.info("My result :{}".format(result))
    return json.dumps(result)


def getNextProbableWords(classes, statements):
  """
  Solution explanation:
  - We have a word repository that contains all possible permutations of strings that might appear in statements.
  - For each statement, we filter out the top 5 words in ascending order that contain the statement as a prefix
  - Space complexity: O(C*F), where C = number of classes, F = number of fields in class.
  - Time complexity: O(C*F)
  """

  word_dump = []

  for class_dict in classes:
    for cls in class_dict:
      word_prefix = cls
      word_dump.append(word_prefix)
      for item in class_dict[cls]:
        word_dump.append(word_prefix + "." + item)

  res = {statement: [] for statement in statements}

  for statement in res:
    res[statement] = sorted(
      list(filter(lambda x: x.startswith(statement), word_dump)))[0:5]
    res[statement] = list(item.split(".")[1]
                          for item in res[statement]) or ['']
  return res