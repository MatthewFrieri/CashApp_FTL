from flask import Flask, jsonify
from flask_cors import CORS
from database import create_connection

app = Flask('server')
CORS(app)

# Example of an endpoint that returns test data
@app.route('/getinfo')
def getinfo():
    info = {"name":'breaking bias', "score":"awesome"}
    return jsonify(info)


@app.route("/database_connection_message")
def open_database():
    connection = create_connection()
    if connection.is_connected():
        message = "Mr Executive, you are connected. Proceed with big boss man activities"
        connection.close()  # Close the connection after checking
    else:
        message = "Failed to connect to the database."
    
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run()