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
SECRET_KEY = '+'
KEY = ''
#URL_PREFIX = 'http://127.0.0.1:5000/play_rayvid?key='
URL_PREFIX = 'http://www.rayvid.com/play_rayvid?key='

@app.route('/')
def hello_world():
   print 'Hello Rayvid.'
   myurl = '/content/IntroVideo.mp4'
   return render_template('index.html', url = myurl, source = "root")

@app.route('/delete', methods=['GET'])
def delete_video():
   print 'Deleting Rayvid.'

   delurl = request.args.get('delurl')
   print "My Delete URL: ", delurl
   dtk = delurl.rsplit('.com/',1)[1] # dtk = "delete this key"
   print "My Delete Key: ", dtk

   conn = S3Connection(ACCESS_KEY, SECRET_KEY)
   bkt = conn.get_bucket('rayvids')
   k = Key(bkt)

   try:
      k.key = dtk
      bkt.delete_key(k)
      print "Delete success."
   except:
      print "Delete failed."

   print "Returning from delete..."

   return "success"

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

         sfile = file.filename.rsplit('.',1)[0].split('-');
         exdel = int(sfile[-1])
         vwdel = int(sfile[-2])

         conn = S3Connection(ACCESS_KEY, SECRET_KEY)
         bkt = conn.get_bucket('rayvids')
         k = Key(bkt)
         ctime = datetime.now()
         keystr = ctime.strftime('%f')
         
         if exdel > 0:
            keystr = 'tmp/'+keystr               
            
         if vwdel > 0:
            keystr = keystr+'_'

         k.key = keystr+'.mp4'
         k.set_contents_from_file(file)
         bkt.set_acl('public-read', k.key)
         url = URL_PREFIX+keystr+'.mp4#agreement'

   return jsonify({"success":True, "url": url})

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
