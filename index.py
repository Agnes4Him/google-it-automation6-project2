#! /usr/bin/env python3

import os
import requests

for file in os.listdir("/data/feedback"):
  file_path = "/data/feedback/" + file
  dict = {}
  filelines = []
  with open(file_path) as f:
    for line in f:
      filelines.append(line)
  dict["title"] = filelines[0].strip()
  dict["name"] = filelines[1].strip()
  dict["date"] = filelines[2].strip()
  dict["feedback"] = filelines[3].strip()
  response = requests.post("http://34.173.143.142/feedback/", json=dict)
  print(response.status_code)

