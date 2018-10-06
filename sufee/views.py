from flask import Flask
from flask import render_template
from flask import abort
from sufee import app

@app.route("/")
@app.route("/home")
def index():
    template = 'index.html'
    return render_template(template)

# @app.route("/about")
# def aboutindex():
#     template = 'about.html'
#     return render_template(template)
#
# @app.route("/azuredeploy")
# def azureindex():
#     template = 'azuredeploy.html'
#     return render_template(template)
#
#
# @app.route("/riots")
# def riots_index():
#     template = 'riots.html'
#     object_list = tutorials.fileimp.get_csv()
#     return render_template(template, object_list=object_list)
#
# @app.route('/riots/<row_id>/')
# def riots_detail(row_id):
#     template = 'riots_detail.html'
#     object_list = tutorials.fileimp.get_csv()
#     for row in object_list:
#         if row['id'] == row_id:
#             return render_template(template, object=row)
#     abort(404)
#
# @app.route("/buildings")
# def buildings_index():
#     template = 'buildings.html'
#     object_buildinglist = tutorials.fileimp.get_buildingscsv()
#     return render_template(template, object_buildinglist=object_buildinglist)
#
# @app.route('/buildings/<row_id>/')
# def buildings_detail(row_id):
#     template = 'buildings_detail.html'
#     object_buildinglist = tutorials.fileimp.get_buildingscsv()
#     for row in object_buildinglist:
#         if row['id'] == row_id:
#             return render_template(template, object=row)
#     abort(404)
