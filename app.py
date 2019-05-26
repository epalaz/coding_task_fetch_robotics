from flask import Flask
import views

app = Flask(__name__)

app.add_url_rule('/', view_func=views.index, methods=['GET'])
app.add_url_rule('/api/maps/', view_func=views.create_map, methods=['POST'])
app.add_url_rule('/api/paths/start/', view_func=views.create_start, methods=['POST'])
app.add_url_rule('/api/paths/goal/', view_func=views.create_goal, methods=['POST'])
app.add_url_rule('/api/costs/', view_func=views.create_heuristic_cost, methods=['POST'])
app.add_url_rule('/api/paths/', view_func=views.find_path, methods=['GET'])

if __name__ == '__main__':
    app.run(port=3000, host='localhost', debug=False)
