from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_identificacion = db.Column(db.String(180), index=True, unique=False, nullable=False)
    numero_identificacion = db.Column(db.String(180), index=True, unique=True, nullable=False)
    nombre  = db.Column(db.String(180), index=True, unique=False, nullable=False)
    edad = db.Column(db.String(180), index=True, unique=False, nullable=False)
    celular = db.Column(db.String(180), index=True, unique=False, nullable=False)
    direccion = db.Column(db.String(180), index=True, unique=False, nullable=False)
    ciudad = db.Column(db.String(180), index=True, unique=False, nullable=False)
    pais = db.Column(db.String(180), index=True, unique=False, nullable=False)

    def __repr__(self):
        return '<Total {}>'.format(self.nombre)