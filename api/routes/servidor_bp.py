from flask import Blueprint

from ..controllers.servidor_controller import Servidor_Controller

servidor_bp = Blueprint('servidor_bp', __name__)

servidor_bp.route('/', methods=['GET'])(Servidor_Controller.get_all)
servidor_bp.route('/<int:id_servidor>', methods=['GET'])(Servidor_Controller.get)
servidor_bp.route('/', methods=['POST'])(Servidor_Controller.create)
servidor_bp.route('/<int:id_servidor>', methods=['PUT'])(Servidor_Controller.update)
servidor_bp.route('/<int:id_servidor>', methods=['DELETE'])(Servidor_Controller.delete)


