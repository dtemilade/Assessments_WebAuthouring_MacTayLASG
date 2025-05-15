from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    domain = request.form.get('domain')
    time = request.form.get('time')

    # query parameter
    if domain == 'domain2':
        return redirect(url_for('domain2', time=time))
    elif domain == 'domain3':
        return redirect(url_for('domain3', time=time))
    elif domain == 'domain4and5':
        return redirect(url_for('domain4and5', time=time))
    else:
        return "Invalid selection."

@app.route('/domain2')
def domain2():
    return render_template('domain2.html')

@app.route('/domain3')
def domain3():
    return render_template('domain3.html')

@app.route('/domain4and5')
def domain4and5():
    return render_template('domain4and5.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
