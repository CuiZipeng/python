

# 1.0 hello word

from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello World'
# 测试函数
if __name__ == '__main__':
    app.run()
from flask import Flask, redirect, url_for, request
app = Flask(__name__)


# 2.0
@app.route('/success/<name>')
def success(name):
	return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['nm']
		return redirect(url_for('success', name=user))
	else:
		user = request.args.get('nm')
		return redirect(url_for('success', name=user))


if __name__ == '__main__':
	app.run(debug=True)
