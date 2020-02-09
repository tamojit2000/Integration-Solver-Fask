from flask import Flask,render_template,request
from sympy import *
from sympy.plotting import plot
#import os

#Connecting_folder=os.path.join('static','img')

app=Flask(__name__)
#app.config['UPLOAD_FOLDER']=Connecting_folder

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result",methods=['POST','GET'])
def result():
    if request.method=='POST':
        x=symbols('x')
        f=eval(request.form['function'])
        u=request.form['upper']
        l=request.form['lower']
        ans=''
##        try:
##            os.remove('static/img/output_graph.jpg')
##        except:
##            pass
        if u=='' and l=='':
            #indefinite
            
            integrated=integrate(f,x)
            p1=plot(f, (x,-20,20),show=False)
            p1.save('static/img/output_graph.jpg')
            ans=integrated
            

        elif u!='' and l!='':
            #definite
            if u.isdigit() and l.isdigit():
                #ok
                l=eval(l)
                u=eval(u)
                definite=integrate(f,(x,l,u))
                p1=plot(f, (x,l,u),show=False)
                p1.save('static/img/output_graph.jpg')
                
                ans=definite
            

            else:
                #error
                ans='Invalid Input'

            pass            
        else:
            #error
            pass
        
#        full_filename=os.path.join(app.config['UPLOAD_FOLDER'],'output_graph.jpg')
        return render_template("result.html",ans=ans,graph="../static/img/output_graph.jpg")

if __name__=='__main__':
    app.run(debug=True)

