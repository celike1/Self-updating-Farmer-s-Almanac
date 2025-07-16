from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def home():
    # Render an HTML template and return
    return render_template('index.html')

@app.route('/for_farmers')
def for_farmers():
    return render_template('forfarmers.html')

@app.route('/for_planters')
def for_planters():
    return render_template('forplanters.html')

if __name__ == '__main__':
    app.run(debug=True)