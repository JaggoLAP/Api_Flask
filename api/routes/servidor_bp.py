from flask import Blueprint

from ..controllers.servidor_controller import ServidorController

servidor_bp = Blueprint('servidor_bp', __name__)

servidor_bp.route('/<int:id_servidor>', methods=['GET'])(ServidorController.get)
servidor_bp.route('/', methods=['GET'])(ServidorController.get_all)
servidor_bp.route('/', methods=['POST'])(ServidorController.create)
servidor_bp.route('/<int:id_servidor>', methods=['PUT'])(ServidorController.update)
servidor_bp.route('/<int:id_servidor>', methods=['DELETE'])(ServidorController.delete)
servidor_bp.route('/user_serv', methods=['POST'])(ServidorController.add_serv)
servidor_bp.route('/<string_param>', methods=['GET'])(ServidorController.get_by_name)
