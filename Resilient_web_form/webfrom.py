#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time
import resilient
from flask import Flask, render_template, request, redirect


time_now = int((time.time() * 1000) //1)

LOG = logging.getLogger('resilient.co3')
LOG.addHandler(logging.StreamHandler())
LOG.setLevel(logging.INFO)

parser = resilient.ArgumentParser(config_file=resilient.get_config_file())
opts = parser.parse_args()
client = resilient.get_client(opts)


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():

    return render_template("index.html")
    #return redirect('https://172.16.178.50/#new')

@app.route('/', methods=['POST'])
def my_form_post():
  name = request.form['submitter_name']
  name_dict ={"name": name}
  email = request.form['submitter_email']
  inc_name = request.form['incident_name']
  inc_type = request.form['incident_type']
  #converting inc_type to a list, because submitter_name expects a list. If inc_type is empty - creating the list [0]
  if not inc_type:
      inc_type = [0]
  else:
      inc_type=inc_type.split("!@#$%^&*")
  inc_text = request.form['incident_text']

  incident = {
      "name": inc_name,
      "description": inc_text,
      "discovered_date": time_now,
      "incident_type_ids": inc_type,
      "properties": {"submitter_name":name},
  }

  client.post("/incidents/", incident)
  msg = "Инцидент " + inc_text + " успешно создан в системе Resilient"
  return render_template("incident_created.html")


if __name__ == "__main__":
    app.run (debug=True)
