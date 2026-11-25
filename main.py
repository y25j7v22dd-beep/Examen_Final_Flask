from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre =  ""
    edad = 0
    cantidad = 0
    total = 0
    descuento = 0
    total_pagar = 0
    porcentaje = 0

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        total = cantidad * 9000

        if edad >= 18 and edad <= 30:
            porcentaje = 0.15
        elif  edad > 30:
            porcentaje = 0.25

        descuento = total * porcentaje
        total_pagar = total - descuento

    return render_template(
        'ejercicio1.html',
        nombre=nombre,
        total=total,
        descuento=descuento,
        total_pagar=total_pagar,
        porcentaje=porcentaje
    )

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""

    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        if usuario == "juan" and contraseña == "admin":
            mensaje = "Bienvenido Administrador juan"
        elif usuario == "pepe" and contraseña == "user":
            mensaje = "Bienvenido Usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template(
        'ejercicio2.html',
        mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)