# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:23:34 2018

@author: Mahesh
"""    
from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)
row=[]
def database():
   
   conn = sqlite3.connect('C:\sqlite\Form.db')
   with conn:
      print("Done")
      cursor=conn.cursor()
   cursor.execute('SELECT * FROM StudentEnroll')
   global row
   row=cursor.fetchall()
   conn.commit()
   
@app.route('/srmsef')
def list():
   database()
   return render_template("backend.html",rows = row)

if __name__ == '__main__':
   app.run(debug = True)