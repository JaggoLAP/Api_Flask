from flask import Blueprint

from ..controllers.mensaje_controller import MensajeController

mensaje_bp = Blueprint('mensaje_bp', __name__)


mensaje_bp.route('/canal/<int:canal_id>',methods=['GET'])(MensajeController.obtener_mensajes_por_canal)
mensaje_bp.route('/', methods=['POST'])(MensajeController.create_mensaje)
mensaje_bp.route('/<int:id_mensaje>', methods=['PUT'])(MensajeController.modificar_mensaje)
mensaje_bp.route('/<int:id_mensaje>', methods=['DELETE'])(MensajeController.borrar_mensaje)