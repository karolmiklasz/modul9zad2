from flask import Flask
from flask_restful import Resource, Api, reqparse
from models import library

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help='Title of the item')
parser.add_argument('description', type=str, help='Description of the item')
parser.add_argument('available', type=bool, help='Availability of the item')

class LibraryResource(Resource):
    def get(self):
        return {'items': library.all()}

    def post(self):
        args = parser.parse_args()
        library.create(args)
        library.save_all()
        return {'message': 'Item created successfully'}, 201

class LibraryItemResource(Resource):
    def get(self, item_id):
        try:
            return {'item': library.get(int(item_id))}
        except IndexError:
            return {'message': 'Item not found'}, 404

    def put(self, item_id):
        args = parser.parse_args()
        try:
            library.update(int(item_id), args)
            return {'message': 'Item updated successfully'}, 200
        except IndexError:
            return {'message': 'Item not found'}, 404

api.add_resource(LibraryResource, '/api/library')
api.add_resource(LibraryItemResource, '/api/library/<item_id>')

if __name__ == '__main__':
    app.run(debug=True)
