#multiple ways to use Jinja2Template
'''
{{   }} expressions to print output
{% %} conditions for loops
{# #}comments
'''

from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/score/<int:score>")
def f(score):
    res=""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template('score.html',results=res)

@app.route("/score_res/<int:score>")
def score(score):
    res = ""
    if score > 50:
        res = "passed"
    else : 
        res = "failed"

    para = {"scores":score,"res":res}
    return render_template('result1.html',results=para)

@app.route("/result_if/<int:score>")
def result_if(score):
    return render_template('result2.html',scores = score)

@app.route("/submit",methods=['POST','GET'])
def submit():
    total = 0
    if request.method == 'POST':
        math = int(request.form['maths'])
        comp = int(request.form['comp'])
        phy = int(request.form['phy'])
        chem = int(request.form['chem'])
        eng = int(request.form['chem'])
        total = (math+comp+phy+chem+eng)/5
    else:
        return render_template('submit.html')
    return redirect(url_for('result_if',score=total))

if __name__ == "__main__":
    app.run(debug=True)