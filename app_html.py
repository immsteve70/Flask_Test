from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>My Flask Page</title>
        </head>
        <body style="font-family: Arial; background-color: #f5f5f5; text-align: center;">
            <h1 style="color: #0078d7;">Welcome to My Flask Website!</h1>
            <p>This is an HTML response directly from Flask</p>
            <a href="/about">Go to About Page</a>
            <a href="/contact">Go to Contact Page</a>
            <a href="/projects">Go to Projects Page</a>
        </body>
    </html>
    """

@app.route('/about')
def about():
    return """
    <html>
        <head>
            <title>About</title>
        </head>
        <body style="font-family: Arial; background-color: #fffbe6; text-align: center;">
            <h1>About Me</h1>
            <p>Hi! I'm Emmanuel, learning Flask slowly and surely 💪</p>
            <a href="/">Back to Home</a>
            <a href="/contact">Go to Contact Page</a>
        </body>
    </html>
    """

@app.route('/contact')
def contacts():
    return """
    <html>
        <head>
            <title>Contact</title>
        </head>
        <body style="font-family: Arial; background-color: #C2E2FA; text-align: center;">
            <h1>Contact Me</h1>
            <p>You can reach me at: immsteve70@gmail.com</p>
            <a href="/">Go Home</a>
            <a href="/about">Go to About Page</a>
        </body>
    </html>
    """

@app.route('/projects')
def projects():
    return """
    <html>
        <head>
            <title>My Projects</title>
        </head>
        <body style="font-family: Arial; background-color: #FFE6D4; text-align: center;">
            <h1>Here are some of my projects</h1>
            <ul>
                <li>To-Do App</li>
                <li>Student Manager</li>
                <li>Portfolio Website</li>
            </ul>
            <a href="/">Go Home</a>
            <a href="/contact">Go to Contacts Page</a>
            <a href="/about">Go to About Page</a>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
