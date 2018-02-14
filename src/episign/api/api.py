import datetime
import simplejson
import urllib2
from flask import Flask, request
from flask import json
import operator

app = Flask(__name__)

message_1 = ''
message_2 = ''

def make_display():
    global message_1
    global message_2
    response = urllib2.urlopen(
        "https://intra.epitech.eu/auth-bbdbc174bc5ed9ab81690345fc20ce7d17a44299/planning/load?format=json&location=FR/MPL&semester=0,1,2,3,4,5,6&start=" + datetime.date.today().strftime(
            "%Y-%m-%d") + "&end=" + datetime.date.today().strftime("%Y-%m-%d"))
    data = simplejson.load(response)
    data = sorted(data, key=lambda k: k['start'])
    messages = []
    for activity in data:
      dateStart = datetime.datetime.strptime(activity['start'], '%Y-%m-%d %H:%M:%S')
      if (dateStart >= datetime.datetime.now()):
        messages.append(activity['acti_title'])
        l_2 = ((activity['start'].split(" ")[1][::-1]).split(":")[2])[::-1] + ":" + ((activity['start'].split(" ")[1][::-1]).split(":")[1])[::-1]
        if activity['room']:
           l_2 += " - " + ((activity['room']['code'][::-1]).split("/")[0])[::-1]
        messages.append(l_2)
    if message_1 != '' and message_2 != '':
        messages.insert(0, message_1)
        messages.insert(0, message_2)
    return messages

@app.route("/send", methods=['POST'])
def send():
    if request.method == 'POST':
        global message_1
        global message_2
        message_1 = request.form['1']
        message_2 = request.form['2']
    data = {}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/display")
def display():
    data = make_display()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
