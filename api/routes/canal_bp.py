from flask import Blueprint

from ..controllers.canal_controller import CanalController

canal_bp = Blueprint('canal_bp', __name__)

canal_bp.route('/<int:id_canal>', methods=['GET'])(CanalController.get)
canal_bp.route('/servidor/<int:servidor_id>', methods=['GET'])(CanalController.get_all)
canal_bp.route('/', methods=['POST'])(CanalController.create)
canal_bp.route('/<int:id_canal>', methods=['PUT'])(CanalController.update)
canal_bp.route('/<int:id_canal>', methods=['DELETE'])(CanalController.delete)