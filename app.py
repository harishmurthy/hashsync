#! bin/python

import web
import json
import hashtree
import filup

urls = (
  '/(.*)', 'syncapp'
)

class syncapp:
  def GET(self,data):
    web.header('Content-Type','application/json')
    fc = hashtree.hashtreeify(data)
    return json.dumps(fc)

  def POST(self,data):
    data = web.data()
    patch = json.loads(data)
    filup.apply(patch)

if __name__ == "__main__":
  app = web.application(urls,globals())
  app.run()
