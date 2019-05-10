from flask import Blueprint

from . import views, errors
from app.models import Permission


main_blueprint = Blueprint('main', __name__)


@main_blueprint.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
