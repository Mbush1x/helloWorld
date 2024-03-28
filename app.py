from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/hello')
def hello():
    return 'Hello World from Madison Bush!'


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():
    print('Entered Subject Name: ' + request.args.get('subject'))
    print('Entered Course Number: ' + request.args.get('course_number'))
      return render_template('favorite-course.html')






if __name__ == '__main__':
    app.run()

