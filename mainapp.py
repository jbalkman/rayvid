# General
import os
import re
from datetime import datetime
from flask import Flask, render_template, jsonify, redirect, url_for, request, send_file

# Storage
from boto.s3.connection import S3Connection
from boto.s3.key import Key

app = Flask(__name__)
app.config.from_object(__name__)

ALLOWED_EXTENSIONS = ['mp4', 'mov']

ACCESS_KEY = ''
SECRET_KEY = ''
KEY = ''
#URL_PREFIX = 'http://127.0.0.1:5000/play_rayvid?key='
URL_PREFIX = 'http://www.rayvid.com/play_rayvid?key='

@app.route('/')
def hello_world():
   print 'Hello Rayvid!'
   myurl = 'https://s3.amazonaws.com/rayvids/IntroVideo.mov'
   return render_template('index.html', url = myurl)

@app.route('/play_rayvid')
def play_rayvid():

   print 'Playing Rayvid'

   conn = S3Connection(ACCESS_KEY, SECRET_KEY)
   bkt = conn.get_bucket('rayvids')

   mykey = request.args.get('key')
   print "My Key: ", mykey
   k = Key(bkt)
   try:
      k.key = mykey
      myurl = k.generate_url(3600).rsplit('?',1)[0]
      print "Here is the URL: ", myurl
      result = 1
   except:
      result = 0
      
   return render_template('index.html', url = myurl)
   #return jsonify({"success":result, "url":url})

@app.route('/upload', methods=['POST'])
def upload():
   
   print "Upload function"
   
   if request.method == 'POST':
      file = request.files['file']
      if file and allowed_file(file.filename):
         #now = datetime.now()

         conn = S3Connection(ACCESS_KEY, SECRET_KEY)
         bkt = conn.get_bucket('rayvids')
         k = Key(bkt)
         ctime = datetime.now()
         ctimestr = ctime.strftime('%f')
         k.key = ctimestr+'.mp4'
         k.set_contents_from_file(file)
         bkt.set_acl('public-read', k.key)
         url = URL_PREFIX+ctimestr+'.mp4'

   return jsonify({"success":True, "url": url})

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
