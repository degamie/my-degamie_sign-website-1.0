from flask import Flask,flash,request,render_template
app=Flask(__name__,template_folder='web-site-degamie_sign')
@app.route('/degamie.com')

def degamiesign():
    return render_template('degamie.html')
    #return "hello ,this is degamiesign"

if __name__== "__main__":
    app.run(host='0.0.0.0',port=5000)