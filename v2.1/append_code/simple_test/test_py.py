from bottle import Bottle, run, template, request, response, redirect, static_file, HTTPError
import json

app=Bottle()


@app.route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='/home/joao/5ano1semestre/ASINT/project/Jquer_learn/Learn-jQuery-in-15-minutes-master')


@app.get('/register')
def register_form():
	a=[1,2,3,4]
	b=['a','b','c','d']
	return template ('test.tpl',numbers=a,letters=b)

actions_adim='''
			<p> Hi <strong>{{user}} </strong> you have been assigned <strong>
			id={{id}} </strong></p>
			<p> Would you like to ...
			</p>
			'''
@app.post('/actions')
def actions_form():

	return template(actions_adim,user=name,id=id)

run(app, host='localhost',port=8080,debug=True)
