from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Vikhlyayeva Alisa TS-91mp!'

@app.route('/first')
def ver1 ():
	a = None
	b = 'First homework'
	c = 24
	return f'{a}, {b}, {c}'
    
if __name__ == '__main__':
	app.run('0.0.0.0')
