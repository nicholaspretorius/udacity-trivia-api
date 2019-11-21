import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import func
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

    @app.route('/')
    def hello_world():
        return jsonify({
            'success': True,
            'ping': 'pong'
        })

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
            abort(500)

    @app.route('/categories/<int:category_id>')
    def retrieve_category_handler(category_id):
        try:
            category = Category.query.get(category_id)

            if category is None:
                abort(404)

            return jsonify({
                'success': True,
                'id': category.id,
                'type': category.type
            })
        except():
            abort(500)

    def retrieve_and_format_questions():
        questions = Question.query.order_by('id').all()
        formatted_questions = [question.format() for question in questions]
        return formatted_questions

    @app.route('/questions', methods=['GET'])
    def retrieve_questions_handler():
        try:
            questions = retrieve_and_format_questions()
            page = request.args.get('page')

            if page:
                paged_questions = paginate_questions(request, questions)
            else:
                paged_questions = questions

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

    @app.route('/questions', methods=['POST'])
    def create_question():
        try:
            body = request.get_json()
            search_term = body.get('search', None)

            if body == {}:
                abort(422)

            # question search
            if search_term is not None:
                search = "%{}%".format(search_term.lower())
                search_results = Question.query.filter(
                    Question.question.ilike(search)).all()
                formatted_search_results = [
                    question.format() for question in search_results]
                paginated_results = paginate_questions(
                    request, formatted_search_results)

                return jsonify({
                    'success': True,
                    'questions': paginated_results,
                    'total_questions': len(search_results)
                })
            # question add
            else:
                question = body.get('question', None)
                answer = body.get('answer', None)
                category = body.get('category', None)
                difficulty = body.get('difficulty', None)

                if question is None or answer is None or category is None or difficulty is None:
                    abort(422)

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

    @app.route('/questions/<int:question_id>')
    def get_question(question_id):
        try:
            question = Question.query.get(question_id)

            if question is None:
                abort(404)

            formatted_question = question.format()

            return jsonify({
                'success': True,
                'question': formatted_question
            })
        except():
            abort(404)

    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_category_questions(category_id):
        try:
            questions = Question.query.filter(
                Question.category == str(category_id)).all()

            category = Category.query.get(str(category_id))

            if category_id < 1 or category is None:
                abort(404)

            if questions is None:
                total_questions = 0
                paginated_questions = []
            else:
                total_questions = [question.format() for question in questions]
                paginated_questions = paginate_questions(
                    request, total_questions)

            return jsonify({
                'success': True,
                'questions': paginated_questions,
                'total_questions': len(total_questions),
                'current_category': Category.query.get(str(category_id)).
                format(),
                'categories': retrieve_categories()
            })

        except():
            abort(500)

    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        try:
            body = request.get_json()

            if body.get('quiz_category') is None or body.get('previous_questions') is None:
                abort(422)

            quiz_category_id = body.get('quiz_category', None)['id']
            previous_questions = body.get('previous_questions', None)

            if quiz_category_id == 0:
                questions = Question.query.order_by(func.random()).all()
            else:
                questions = Question.query.\
                    filter(
                        Question.category == quiz_category_id).\
                    order_by(func.random()).all()

            formatted_questions = [question.format() for question in questions]
            available_questions = []
            for q in formatted_questions:
                if len(previous_questions) == 0:
                    available_questions.append(q)
                elif len(previous_questions) >= 0:
                    found = q['id'] not in previous_questions
                    if found is True:
                        available_questions.append(q)

            if len(available_questions) > 0:
                return jsonify({
                    'success': True,
                    'question': available_questions[0]
                })
            else:
                return jsonify({
                    'success': True,
                    'question': None
                })
        except():
            abort(422)

    @app.errorhandler(400)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

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
