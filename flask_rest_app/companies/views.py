from datetime import datetime
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from .models import Company
from .schemas import company_to_dict, dict_to_company
from .. import db

app = Blueprint('companies', __name__, url_prefix='/companies')
  

@app.route('/', methods=['POST'])
def add_company():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    company = dict_to_company(data)
    db.session.add(company)
    db.session.commit()
    return jsonify(company_to_dict(company)), 201


@app.route('/<int:id>', methods=['DELETE'])
def delete_company(id):
    company = Company.query.filter_by(id=id).first()

    if not company:
        return jsonify({'error': f'Company not found: {id}'}), 404

    db.session.delete(company)
    db.session.commit()

    return '', 204


@app.route('/<int:id>', methods=['GET'])
def get_company(id):
    company = Company.query.filter_by(id=id).first()

    if not company:
        return jsonify({'error': f'Company not found: {id}'}), 404

    return jsonify(company_to_dict(company))


@app.route('/', methods=['GET'])
def list_companies():
    name = request.args.get('name')
    order_by = request.args.get('order_by', 'name')
    offset = int(request.args.get('offset', 0))
    limit = int(request.args.get('limit', 10))
    
    query = Company.query

    if name:
        query = query.filter(func.lower(Company.name).contains(func.lower(name)))
    
    # Simple sorting
    if order_by == 'name':
        query = query.order_by(Company.name)
    elif order_by == 'id':
        query = query.order_by(Company.id)
    elif order_by == 'country_code':
        query = query.order_by(Company.country_code)
    else:
        query = query.order_by(Company.name)
    
    if offset:
        query = query.offset(offset)
    if limit:
        query = query.limit(limit)

    companies = query.all()
    return jsonify([company_to_dict(company) for company in companies])


@app.route('/<int:id>', methods=['POST', 'PATCH'])
def update_company(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    company = Company.query.filter_by(id=id).first()

    if not company:
        return jsonify({'error': f'Company not found: {id}'}), 404

    company.name = data.get('name', company.name)
    company.country_code = data.get('country_code', company.country_code)
    company.website = data.get('website', company.website)
    company.enabled = data.get('enabled', company.enabled)
    company.updated_at = datetime.now()
    
    db.session.commit()

    return jsonify(company_to_dict(company))
