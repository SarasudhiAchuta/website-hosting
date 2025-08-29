from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', 'Friend')
        message = request.form.get('message', '')
        # In a real app, you'd store or email this. For now, just thank the user.
        return render_template('thanks.html', name=name, title='Thanks')
    return render_template('contact.html', title='Contact')

@app.route('/api/hello')
def api_hello():
    return jsonify(message="Hello from Flask API!")

if __name__ == '__main__':
    # For development only. In production, use gunicorn (see README).
    app.run(debug=True)