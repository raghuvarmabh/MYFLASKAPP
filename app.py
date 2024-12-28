from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
#    return "<h2>Hello, Flask!</h2>"
    return render_template('index.html', message="Hello from Flask!")

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Access form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Process the data (example: just return it as a response)
    return f"""
    <h1>Form Submitted</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Message:</strong> {message}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

