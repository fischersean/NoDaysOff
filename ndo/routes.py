from calendar import Calendar
from flask import current_app as app
from flask import render_template, request, send_from_directory


@app.route("/", methods=["GET"])
def home():
    return render_template("calendar2020.html")


@app.route("/styles/<path:path>")
def send_css(path):
    print("HEHEHE")
    return send_from_directory("static/styles", path)


@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory("static/js", path)


@app.route("/api/monthnames", methods=["GET"])
def apiv1getmnames():
    month_names = [
        "JAN",
        "FEB",
        "MAR",
        "APR",
        "MAY",
        "JUN",
        "JUL",
        "AUG",
        "SEP",
        "OCT",
        "NOV",
        "DEC",
    ]
    return month_names


@app.route("/api/getcal", methods=["GET"])
def apiv1getcal():
    year = request.args.get("year", default=2020, type=int)

    month_names = apiv1getmnames()
    cal = Calendar(6).yeardayscalendar(year, width=12)[0]
    ret_dict = {}
    for month, month_name in zip(cal, month_names):
        tmpdict = {}
        for i, week in enumerate(month):
            tmpdict[str(i)] = week
        ret_dict[month_name] = tmpdict

    return ret_dict
