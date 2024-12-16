from flask import Flask

def register_blueprints(app: Flask):
    from .planning import planning_bp
    app.register_blueprint(planning_bp)