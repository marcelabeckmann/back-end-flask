from flask.views import MethodView
from flask import Blueprint, request

categories_blueprint = Blueprint("categories_blueprint", __name__, url_prefix='/api/')

class CategoriesList(MethodView):
    def get(self):

        return [{ "category": "Category1"}, {"category": "Category2"}, {"category": "Category3"}]

class CategoriesID(MethodView):
    def get(self, category_id):

        return { "id": category_id, "category": "Category1"}
    
class Categories(MethodView):
    def post(self):
        data = request.get_json()

        category = data.get('category')

        if category is None:
            return {"message": "No has ingresado categoria"}, 400
        
        return {"message": "Nueva categoria!"}


    
categories_blueprint.add_url_rule(
    'categories',
    view_func=CategoriesList.as_view("categories_list")
)
categories_blueprint.add_url_rule(
    'categories',
    view_func=Categories.as_view("categories")
)
categories_blueprint.add_url_rule(
    'categories/<category_id>',
    view_func=CategoriesID.as_view("category_id")
)