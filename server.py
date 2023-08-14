from flask import Flask, render_template, request, redirect
import os
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


@app.route("/scan", methods=['POST', 'GET'])
def scan_info():
	if request.method == 'POST':
		with open('scope.txt', 'r') as scope:
			with open('result.txt', 'a') as res:
				for line1 in scope:
					line1 = line1.replace("\n", "")
					line = line1.replace(".", "").replace("\n", "")
					os.system(f"nmap -sV -sC -oN {line}-nmap.txt -T4 {line1}")
					os.system(f"nuclei -u {line1} -o {line}-nuclei.txt")
					os.system(f"gobuster dir -u {line1} -w wordlists/dirs.txt > {line}-dirs")
					os.system(f"gobuster fuzz -u FUZZ.{line1} -w wordlists/subs.txt > {line}-subs.txt")
					with open(f'{line}-nmap.txt', 'a') as nmap:
						res.write(f"Nmap {line} results:\n\n" + nmap.read())
					with open(f'{line}-nuclei.txt', 'a') as nmap:
                                                res.write(f"Nuclei {line} results:\n\n" + nmap.read())
					with open(f'{line}-dirs.txt', 'a') as nmap:
                                                res.write(f"Directories {line} results:\n\n" + nmap.read())
					with open(f'{line}-subs.txt', 'a') as nmap:
                                                res.write(f"Subdomains {line} results:\n\n" + nmap.read())
					return render_template("scan-info.html", result=res.read())
	else:
		return render_template("scan-info.html")

@app.route("/check")
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

