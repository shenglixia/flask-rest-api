from .models import Company


def company_to_dict(company):
    """Convert Company model to dictionary"""
    return {
        'id': company.id,
        'name': company.name,
        'country_code': company.country_code,
        'website': company.website,
        'enabled': company.enabled,
        'updated_at': company.updated_at.isoformat() if company.updated_at else None,
        'created_at': company.created_at.isoformat() if company.created_at else None
    }


def dict_to_company(data):
    """Convert dictionary to Company model"""
    return Company(
        name=data.get('name'),
        country_code=data.get('country_code'),
        website=data.get('website'),
        enabled=data.get('enabled', True)
    )
