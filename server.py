from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def main():
	return render_template("index.html")

@app.route("/scope", methods = ['POST', 'GET'])
def scope():
	if request.method == 'POST':
		with open('scope.txt', 'a') as f:
			f.write(request.form['scope'] + '\n')
	with open('scope.txt', 'r') as f:
		scope = f.read().split("\n")
	return render_template("scope.html", scope_text=scope)


@app.route("/scan-info")
def scan_info():
        return render_template("index.html")

@app.route("/scan-vulnerabilities")
def scan_vulns():
        return render_template("index.html")

@app.route("/exploits")
def exploits():
        return render_template("index.html")

@app.route("/settings")
def settings():
        return render_template("index.html")
@app.route("/clear", methods=['POST'])
def clear_scope():
	if request.method == 'POST':
		with open('scope.txt', 'w') as f:
			f.write('')
	return redirect('/scope')
app.run()

