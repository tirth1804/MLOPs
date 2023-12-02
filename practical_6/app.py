# from flask import Flask, render_template
# app = Flask(__name__)

# # Define your routes and views here

# @app.route('/')
# def home():
#     return render_template('index.html', title='Home')

# # Add more routes and views as needed

# if __name__ == '__main__':
#     # Run the Flask app
#     app.run(debug=True, host='0.0.0.0', port=80)


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is your Flask app!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
