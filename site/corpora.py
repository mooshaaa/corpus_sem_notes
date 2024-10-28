from db_search_multiple_docs import *

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Corpora1.html')

@app.route('/process', methods=['POST'])
def s():
    q = request.form['req']
    db_file='sem_notes_corp.db' # проверь, что там с ссылкой на папку в pev
    # разберись с множественным выбором
    doc_name=request.form.getlist('exampleRadios')
    if len(doc_name) == 0:
        doc_name = None
    else:
        doc_name = [str(i)+"." for i in doc_name]
    try:
        gender = request.form['tvo']
    except KeyError:
        gender = None

    result = search(q, db_file, doc_name, gender)
    res = zip(list(result.keys()), ['|'.join(list(i.values())[:-1])+"|2023" for i in list(result.values())])
    return render_template('Corpora2.html', a=res, question=q)


if __name__ == '__main__':
    app.run(debug=True)
