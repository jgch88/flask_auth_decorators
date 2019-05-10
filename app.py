from flask import Flask
from authDecorator import roles_required
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/get_test_questions/<string:role>', methods=['GET'])
@roles_required(['teacher', 'principal'])
def get_test_questions(role):
    return 'Q1: What is the meaning of life?'

@app.route('/get_exam_result/<int:student_id>')
@roles_required(['student', 'teacher', 'principal'])
def get_exam_result(student_id):
    return 'You got 100 marks'
