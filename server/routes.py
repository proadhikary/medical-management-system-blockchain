from flask import Blueprint, request, jsonify
from .database import db
from models.patient import Patient
from models.doctor import Doctor
from models.record import MedicalRecord

def init_routes(app):
    main = Blueprint('main', __name__)

    @main.route('/patients', methods=['GET'])
    def get_patients():
        patients = Patient.query.all()
        return jsonify([p.serialize() for p in patients])

    @main.route('/doctors', methods=['GET'])
    def get_doctors():
        doctors = Doctor.query.all()
        return jsonify([d.serialize() for d in doctors])

    @main.route('/records', methods=['POST'])
    def add_record():
        data = request.get_json()
        new_record = MedicalRecord(**data)
        db.session.add(new_record)
        db.session.commit()
        return jsonify(new_record.serialize()), 201

    app.register_blueprint(main)
