import re
import http_format as http
import config;

def index(body, headers, success=""):
    conf = config.get()
    success_result = ""
    if success == True:
      success_result = '<div class="rounded-circle bg-success text-light m-3 p-2 d-inline">&#10004;</div>'
    if success == False:
      success_result = '<div class="rounded-circle bg-danger text-light m-3 p-2 d-inline">&#215;</div>'

    return http.ok('''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title>sonde</title>
  </head>
  <body>
    <h1 class="h2 text-primary text-center">Sonde Temperature</h1>
    <form class="m-5">
      <div class="form-group"><label for="ssid">SSID</label><input class="form-control" type="text" name="ssid" value="{0}"></div>
      <div class="form-group"><label for="password">Password</label><input class="form-control" type="text" name="password" value="{1}"></div>
      <div class="form-group"><label for="server">Serveur</label><input class="form-control" type="text" name="server" value="{2}"></div>
      <button type="submit" formmethod="post" class="btn btn-primary">Envoyer</button>
      {3}
    </form>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
'''.format(conf['ssid'], conf['password'], conf['server'], success_result))

def post(body, headers):
    m = re.search('ssid=(\w+)&password=(\w+)&server=(\w+)', body)
    if (m):
      conf = config.get();
      conf['ssid'] = m.group(1);
      conf['password'] = m.group(2);
      conf['server'] = m.group(3);
      config.set(conf)
      config.save()
      success = True
    else:
      success = False
    return index(body, headers, success)

def option(body, headers):
     return http.json('')


