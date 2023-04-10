
# Function to search the stock item by food ID.
def search_stock_item(fid, stock_data):
    stock_item = [stock for stock in stock_data if stock["f_id"] == fid]
    return stock_item


def get_index(fid, stock_data):
    for index, stock_data in enumerate(stock_data):  # enumerates assign an index for each item in the stock
        if stock_data["f_id"] == fid:
            return index
    return -1
