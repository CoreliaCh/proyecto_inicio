from flask import Flask, render_template, request, redirect, session   
app = Flask(__name__)    
app.secret_key = 'secreto'

@app.route('/')
def index():   
    if 'num' in session:
        session['num'] += 1
    else:
        session['num'] = 0
    return render_template("index.html")

@app.route('/limpiar')
def limpiar():   
    session.clear()    
    return redirect('/')

@app.route('/doblecontador')
def doble():
    session['num'] += 1
    return redirect('/')   

@app.route('/destroy_session')
def destruir_session():   
    session.clear()    
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return "PAGINA NO ENCONTRADA"

if __name__=="__main__":  
    app.run(debug=True)   