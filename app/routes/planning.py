from flask import Blueprint, render_template

planning_bp = Blueprint('planning', __name__)

@planning_bp.route('/planning')
def planning():
    return render_template('planning/index.html')
