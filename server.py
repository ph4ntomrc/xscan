from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
	return render_template("index.html")

@app.route("/scope")
def scope():
        return render_template("scope.html")

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


app.run()
