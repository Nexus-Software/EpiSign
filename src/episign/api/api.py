import datetime
import simplejson
import urllib2
from flask import Flask
from flask import json

app = Flask(__name__)


def make_display():
    response = urllib2.urlopen(
        "https://intra.epitech.eu/auth-7d3c35a078f73117aa5e6606fa25c727065e674a/planning/load?format=json&location=FR/MPL&semester=0,1,2,3,4,5,6&start=" + datetime.date.today().strftime(
            "%Y-%m-%d") + "&end=" + datetime.date.today().strftime("%Y-%m-%d"))
    data = simplejson.load(response)
    messages = []
    for activity in data:
      dateStart = datetime.datetime.strptime(activity['start'], '%Y-%m-%d %H:%M:%S')
      if (dateStart <= datetime.datetime.now()):
        messages.append(activity['acti_title'])
        l_2 = ((activity['start'].split(" ")[1][::-1]).split(":")[2])[::-1] + ":" + ((activity['start'].split(" ")[1][::-1]).split(":")[1])[::-1]
        if activity['room']:
           l_2 += " - " + ((activity['room']['code'][::-1]).split("/")[0])[::-1]
        messages.append(l_2)
    return messages


@app.route("/display")
def display():
    data = make_display()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
