from flask_restful import Resource


# noinspection PyMethodMayBeStatic
class hello(Resource):
    def get(self):
        return {'text': 'hello world'}

