from flask import Flask
from flask import render_template
from flask import abort
from sufee import app

@app.route("/")
@app.route("/home")
def index():
    template = 'index.html'
    return render_template(template)

@app.route("/page-login")
def login():
    template = "page-login.html"
    return render_template(template)

@app.route("/page-register")
def register():
    template = "page-register.html"
    return render_template(template)

@app.route("/pages-forget")
def page_forget():
    template = 'pages-forget.html'
    return render_template(template)

# @app.route("/about")
# def aboutindex():
#     template = 'about.html'
#     return render_template(template)
#

@app.route("/ui-buttons")
def ui_buttons():
    template = 'ui-buttons.html'
    return render_template(template)

@app.route("/ui-badges")
def ui_badges():
    template = 'ui-badges.html'
    return render_template(template)


@app.route("/ui-tabs")
def ui_tabs():
    template = 'ui-tabs.html'
    return render_template(template)

@app.route("/charts-chartjs")
def charts_chartjs():
    template = 'charts-chartjs.html'
    return render_template(template)

@app.route("/charts-flot")
def charts_flot():
    template = 'charts-flot.html'
    return render_template(template)

@app.route("/charts-peity")
def charts_peity():
    template = '/charts-peity.html'
    return render_template(template)

@app.route("/font-fontawesome")
def font_fontawesome():
    template = 'font-fontawesome.html'
    return render_template(template)

@app.route("/font-themify")
def font_themify():
    template = 'font-themify.html'
    return render_template(template)

@app.route("/font-advanced")
def font_advanced():
    template = 'font-advanced.html'
    return render_template(template)

@app.route("/forms-basic")
def forms_basic():
    template = 'forms-basic.html'
    return render_template(template)

@app.route("/forms-advanced")
def forms_advanced():
    template = 'forms-advanced.html'
    return render_template(template)

@app.route("/frame")
def frame():
    template = 'frame.html'
    return render_template(template)

@app.route("/maps-gmap")
def maps_gmap():
    template = 'maps-gmap.html'
    return render_template(template)

@app.route("/maps-vector")
def maps_vector():
    template = 'maps-vector.html'
    return render_template(template)

@app.route("/tables-basic")
def tables_basic():
    template = 'tables-basic.html'
    return render_template(template)

@app.route("/tables-data")
def tables_data():
    template = 'tables-data.html'
    return render_template(template)

@app.route("/ui-alerts")
def ui_alerts():
    template = 'ui-alerts.html'
    return render_template(template)

@app.route("/ui-cards")
def ui_cards():
    template = 'ui-cards.html'
    return render_template(template)

@app.route("/ui-grids")
def ui_grids():
    template = 'ui-grids.html'
    return render_template(template)

@app.route("/ui-modals")
def ui_modals():
    template = 'ui-modals.html'
    return render_template(template)

@app.route("/ui-progressbar")
def ui_progressbar():
    template = 'ui-progressbar.html'
    return render_template(template)

@app.route("/ui-social-buttons")
def ui_social_buttons():
    template = 'ui-social-buttons.html'
    return render_template(template)

@app.route("/ui-switches")
def ui_switches():
    template = 'ui-switches.html'
    return render_template(template)

# @app.route("/ui-tabs")
# def ui_tabs():
#     template = 'ui-tabs.html'
#     return render_template(template)

@app.route("/ui-typography")
def ui_typography():
    template = '/ui-typography.html'
    return render_template(template)

@app.route("/widgets")
def widgets():
    template = 'widgets.html'
    return render_template(template)

