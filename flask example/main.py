from flask import Flask, jsonify

app = Flask(__name__)
books = [
    {
        'id': 0,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'first_sentence': 'The coldsleep itself was dreamless.',
        'year_published': '1992'
    },
    {
        'id': 1,
        'title': 'The Ones Who Walk Away From Omelas',
        'author': 'Ursula K. Le Guin',
        'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to '
                          'the city Omelas, bright-towered by the sea.',
        'published': '1973'
    },
    {
        'id': 2,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
        'published': '1975'
    }
]


@app.route('/get_all')
def get_all():
    response = jsonify(books)
    return response


@app.route('/get_by_id/<book_id>', methods=['GET'])
def get_by_id(book_id):
    return books[int(book_id)]


@app.route('/save', methods=['POST'])
def save():
    return


if __name__ == '__main__':
    app.run()
