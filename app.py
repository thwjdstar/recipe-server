# flask 프레임워크를 이용한, Restful API 서버 개발 

from flask import Flask 
from flask_restful import Api

from resources.recipe import RecipeListResource, RecipeResource

app = Flask(__name__)

api = Api(app)

# API를 구분해서 실행시키는 것은, 
# HTTP Method와 url의 조합이다.

# 경로(path)와 리소스(API코드)를 연결한다.
api.add_resource( RecipeListResource , '/recipes' )
api.add_resource( RecipeResource, '/recipes/<int:recipe_id>')

if __name__ == '__main__':
    app.run()