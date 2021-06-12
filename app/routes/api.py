import os
from app import app, db
from app.models import User
from flask import render_template, redirect, url_for, request
from app.forms import RegistrationForm
from wtforms.validators import ValidationError

basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    registros = User.query.order_by(User.id.desc()).paginate(
        page, 10, False)
    next_url = url_for('explore', page=registros.next_num) \
        if registros.has_next else None
    prev_url = url_for('explore', page=registros.prev_num) \
        if registros.has_prev else None
    return render_template('index.html', registros=registros.items,
                            next_url=next_url, prev_url=prev_url)

@app.route('/registro', methods=['GET', 'POST'])
def registr_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        if(form.validate_identification(form.numero_identificacion.data) == True):
            form.numero_identificacion.errors += (ValidationError("El usuario ya existe"),)
        else:
            user = User(tipo_identificacion=form.tipo_identificacion.data,
                        numero_identificacion=form.numero_identificacion.data,
                        nombre=form.nombre.data,
                        edad=form.edad.data,
                        celular=form.celular.data,
                        direccion=form.direccion.data,
                        ciudad=form.ciudad.data,
                        pais=form.pais.data)
            db.session.add(user)
            db.session.commit()
            return redirect('http://localhost:5000/')

    return render_template('registro.html',form=form)


@app.route('/eliminar/<id>', methods=['GET', 'POST'])
def eliminar(id):
    User.query.filter(User.id == id).delete()
    db.session.commit()
    return redirect('http://localhost:5000/')

