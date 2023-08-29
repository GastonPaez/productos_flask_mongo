from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import redirect
from flask import url_for
import database as dbase
from product import Product
app = Flask(__name__)

db = dbase.dbConnection()


@app.route('/')
def home():
    products = db['products']
    # Obtiene la DDBB
    productsReceived = products.find()
    # Poniendo products en el parametro se puede acceder desde el html
    return render_template('index.html', products = productsReceived)


@app.route('/products', methods=['POST'])
def addProduct():
    # Crea la collection
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        product = Product(name, price, quantity)
        # La instancia de la collection aplica en el formato que se definio en la clase
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'name': name,
            'price': price,
            'quantity': quantity
        })
        return redirect(url_for('home'))
    else:
        return not_found()


@app.errorhandler(404)
def not_found(errorNone):
    message = {
        'message': "Pagina no encontrada" + request.url,
        'status': "404 Not Found"
    }
    response = jsonify(message)
    response.status_code = 404
    return response


@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    # Funcion de mongodb
    products.delete_one({'name': product_name})
    return redirect(url_for('home'))


@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        products.update_one(
            {'name': product_name},
            {'$set':
                {
                    'name': name,
                    'price': price,
                    'quantity': quantity
                }
             })
        response = jsonify({'message': 'Producto ' + product_name + " actualizado"})
        return redirect(url_for('home'))
    else:
        return not_found()


if __name__ == '__main__':
    app.run(debug=True, port=800)
