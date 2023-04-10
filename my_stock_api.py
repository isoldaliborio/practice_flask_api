

from flask import Flask, jsonify, request
from stock_data import stock_food_data
from utils import search_stock_item, get_index
app = Flask(__name__)


# main test page - wellcome test.
@app.route("/")
def wellcome():
    return {"text": "Wellcome to your Home Stock"}  # This must be in a dictionary value?


# page with all stock information.
@app.route("/stock")
def get_stock():
    return stock_food_data


# page shows an item from a given item ID.
@app.route("/stock/<int:id>")  # <int:id> is <datatype:id argument come from the URL input>
def get_stock_by_id(fid):
    stock_item = search_stock_item(fid, stock_food_data)  # stock_food_data is imported from stock_data file
    return jsonify(stock_item)


@app.route("/stock", methods=["POST"])
def add_item():
    item = request.get_json()  # get.json gets the information from our request
    stock_food_data.append(item)
    return item


@app.route("/stock/<int:fid>", methods=["PUT"])
def update_item(fid):
    item_to_update = request.get_json()
    index = get_index(fid, stock_food_data)  # function in utils
    if index != -1:
        stock_food_data[index] = item_to_update
        return stock_food_data[index]


@app.route("/stock/<int:fid>", methods=["DELETE"])
def delete_item(fid):
    index = get_index(fid, stock_food_data)
    deleted = stock_food_data.pop(index)
    # pop() method removes the element at the specified position
    return jsonify(deleted)


if __name__ == "__main__":
    app.run(debug=True)
