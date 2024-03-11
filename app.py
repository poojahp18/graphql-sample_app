import graphene
from graphene import ObjectType, String, List
from flask import Flask,request,jsonify

app = Flask(__name__)


class BookType(ObjectType):
    title = String()
    author = String()

class Query(ObjectType):
    books = List(BookType)

    def resolve_books(self,info):
        return [
            BookType(title = "Book 1", author="Author 1"),
            BookType(title = "Book 2", author="Author 2")
        ]
    
schema = graphene.Schema(query = Query)

@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    query = data.get('query')
    result = schema.execute(query)
    return jsonify(result.data)


if __name__ == "__main__":
    app.run()