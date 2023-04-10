
## Steps to start

# First install Flask:

- pip3 install flask

# Create a file where your flask routes are going to live

- file: my_stock_api.py
  - Display data (get requests)
    - main - / route: test page 
    - /stock route: display all stock data 
    - stock route/id:

  - Manipulate data (post, delete, others requests)
    - /stock, methods=["POST"]
    - 

# Create a utils file to store your functions

- file: utils.py
  - function to find item by id. This function will be called from the route function

# Create a client-side file to send the requests and display info

- file: client_side.py

# Now we just need a fake data file to act as the DB in this first iteration, and then populate the file with dummy data.

- file: stock_data.py


On stock_api
- imports
- @app.route(/method)
- Function