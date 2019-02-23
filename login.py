from flask import Flask,render_template,request,make_response


app=Flask(__name__)

@app.route('/')
def input():
    return render_template('login1.html')

@app.route('/details',methods=['POST','GET'])
def details():
    return render_template('detail.html')

@app.route('/current_emp',methods=['POST','GET'])
def current_emp():
    resp= make_response(render_template('info_CE.html'))
    return resp

@app.route('/new_emp')
def new_emp():
    return render_template('info_NE.html')

@app.route('/destination1',methods=['POST','GET'])
def destination():
    return render_template('destination1.html')

if __name__=='__main__':
    app.run(debug=True)