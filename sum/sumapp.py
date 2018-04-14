from flask import Flask
from flask_restful import Resource, Api
import socket
from datetime import datetime

app = Flask(__name__)
api = Api(app)


class Mydetails(Resource):
    def get(self):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {'IP': socket.gethostbyname(socket.gethostname()),
                'Date': date}


api.add_resource(Mydetails, '/details')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5555)
