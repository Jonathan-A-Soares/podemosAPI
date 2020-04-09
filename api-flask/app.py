from flask import Flask, jsonify

app = Flask(__name__)


devs = [{
    'id': 1,
    'lang': 'Bruno',
    'Profissão':'Desenvolvedor',
    'idade': 26,
    'status':'Solteiro'
},
{   'id': 2,
    'lang': 'Jacinto',
    'Profissão':'Vendedor',
    'idade': 26,
    'status':'Casado'},

{   'id': 3,
    'lang': 'Juliano',
    'Profissão':'Designer',
    'idade': 4,
    'status':'Casado'},

{   'id': 4,
    'lang': 'Rodrigo',
    'Profissão':'Vendedor',
    'idade': 26,
    'status':'Casado'}


]

@app.route('/devs')
def home():
    return jsonify(devs),200

@app.route('/devs/<string:lang>',methods=['GET'])
def devs_nomes(lang):
    devs_nomes =[dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_nomes),200

@app.route('/devs/<int:id>',methods=['GET'])
def dev_id(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200
    return jsonify({'error':'not found'}), 404

if __name__ =='__main__':
    app.run(debug=True)