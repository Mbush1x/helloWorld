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


@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject', '')
    course_number = request.args.get('course_number', '')
    print('Entered Subject Name: ' + subject)
    print('Entered Course Number: ' + course_number)
    return render_template('favorite-course.html', subject=subject, course_number=course_number)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print('Entered First Name: ' + request.form.get('firstName'))
        print('Entered Last Name: ' + request.form.get('lastName'))
        print('Entered Email Address: ' + request.form.get('email'))
        return render_template('contact.html', submitted = True)
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()

