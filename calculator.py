from flask import Flask,render_template,request,make_response
app=Flask(__name__)

@app.route('/')
def input():
    return render_template('page2.html')

@app.route('/page3',methods=['POST','GET'])
def page3():
    a=request.form.get('nos1',type=int)
    b=request.form.get('nos2',type=int)
    result=a+b
    resp=make_response(render_template('page3.html',result=result))
    resp.set_cookie('result',str(result))
    return resp


@app.route('/page4',methods=['POST','GET'])
def page4():
    c = request.form.get("nos3", type=int)
    result=int(request.cookies.get('result'))
    final_output=c+result
    return render_template('page4.html',result_1=str(final_output))
if __name__=='__main__':
    app.run(debug=True)