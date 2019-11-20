import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, questions):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    current_questions = questions[start:end]
    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    '''
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    '''
    def retrieve_categories():
        categories = Category.query.order_by('id').all()
        formatted_categories = [category.format() for category in categories]
        return formatted_categories

    @app.route('/categories')
    def retrieve_categories_handler():
        try:
            categories = retrieve_categories()

            return jsonify({
                'success': True,
                'categories': categories,
                'total': len(categories),
            })
        except():
            return abort(500)

    @app.route('/categories/<int:category_id>')
    def retrieve_category_handler(category_id):
        try:
            category = Category.query.get(category_id)

            if category is None:
                abort(404)

            return jsonify({
                'id': category.id,
                'type': category.type
            })
        except():
            abort(500)

    '''
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for
    three pages. Clicking on the page numbers should update the questions.
    '''
    def retrieve_and_format_questions():
        questions = Question.query.order_by('id').all()
        formatted_questions = [question.format() for question in questions]
        return formatted_questions

    @app.route('/questions')
    def retrieve_questions_handler():
        try:
            questions = retrieve_and_format_questions()
            paged_questions = paginate_questions(request, questions)
            categories = retrieve_categories()

            return jsonify({
                'success': True,
                'questions': paged_questions,
                'total_questions': len(questions),
                'current_category': None,
                'categories': categories
            })
        except():
            return abort(500)

    '''
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will
    be removed. This removal will persist in the database and when you refresh
    the page.
    '''
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.get(question_id)

            if question is None:
                abort(404)

            question.delete()
            questions = retrieve_and_format_questions()
            paged_questions = paginate_questions(request, questions)

            return jsonify({
                'success': True,
                'deleted': question.id,
                'questions': paged_questions,
                'total_questions': len(questions)
            })

        except():
            abort(422)

    '''
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last
    page of the questions list in the "List" tab.
    '''
    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()
        print('JSON: ', body)

        question = body.get('question', None)
        answer = body.get('answer', None)
        category = body.get('category', None)
        difficulty = body.get('difficulty', None)

        try:
            new_question = Question(
                question=question, answer=answer, category=category,
                difficulty=difficulty)
            new_question.insert()

            total_questions = retrieve_and_format_questions()
            paged_questions = paginate_questions(request, total_questions)

            return jsonify({
                'success': True,
                'created': new_question.id,
                'questions': paged_questions,
                'total_questions': len(total_questions)
            })

        except():
            abort(422)

    '''
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    '''

    '''
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    '''

    '''
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    '''

    '''
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    return app
