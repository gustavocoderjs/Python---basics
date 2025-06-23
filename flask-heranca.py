

# base_view.py
from flask import request, jsonify
from flask.views import MethodView

class BaseAPI(MethodView):
    def dispatch_request(self, *args, **kwargs):
        # Exemplo simples de log ou autenticação
        print(f"[LOG] Acessando: {request.path}")
        return super().dispatch_request(*args, **kwargs)
    
    def response_ok(self, data):
        return jsonify({"status": "ok", "data": data})

# produto_view.py
