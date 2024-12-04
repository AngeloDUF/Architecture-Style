from flask import Flask, request, jsonify
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return f"Hello, {name}!"

schema = graphene.Schema(query=Query)

app = Flask(__name__)

@app.route('/graphql', methods=['GET', 'POST'])
def graphql_server():
    if request.method == 'POST':
        # Realizar la consulta GraphQL
        query = request.json.get('query')
        result = schema.execute(query)
        return jsonify(result.data)
    return '''
        <form method="post">
            <textarea name="query">{ hello }</textarea>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True, port=5000)

