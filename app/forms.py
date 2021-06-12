from flask_wtf import FlaskForm
from app.models import User
from wtforms import StringField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    tipo_identificacion = StringField('Tipo Identificacion', validators=[DataRequired()])
    numero_identificacion = StringField('Numero Identificacion', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    edad = StringField('Edad', validators=[DataRequired()])
    celular = StringField('Celular', validators=[DataRequired()])
    direccion = StringField('Direccion', validators=[DataRequired()])
    ciudad = StringField('Ciudad', validators=[DataRequired()])
    pais = StringField('Pais', validators=[DataRequired()])

    def validate_identification(self, number):
        user = User.query.filter_by(numero_identificacion=number).first()
        if user is not None and user.numero_identificacion != self.numero_identificacion:
            return True
        else:
            return False