# Full Stack API Final Project

## Full Stack Trivia

### Introduction

The Trivia App enables you to play a trivia game along with viewing and creating trivia questions and answers for that game. Trivia questions each have a: question, answer, category and a difficulty rating.

### Getting Started

In order to get the application running on your machine you need to do the following:

#### Pre-requisites

You need to have Git, Python3, pip3, Postgresql and Node installed on your machine. 

#### Code

To checkout the code, run: `git clone https://github.com/nicholaspretorius/udacity-trivia-api.git`
Once the project is on your computer, change into the project directory: `cd udacity-trivia-api`

#### Database

Run: `createdb trivia` for the app database
Run: `createdb trivia_test` for the test database

#### Backend

Change into your backend folder: `cd backend`
To install the dependencies, run: `pip install requirements.txt`
To run the app, run: 
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

The API will no be running on: http://localhost:5000/. You should see a JSON response containing: 

```
{
    "ping": "pong",
    "success": true
}
```

#### Tests

To run the tests, do the following from the /backend folder:

`dropdb trivia_test`
`creatdb trivia_test`
`psql trivia_test < trivia.psql`
`python test_flaskr.py`

If you are running the tests for the first time, you can omit the `dropdb command`.

#### Frontend

Change into the /frontend folder. 

From there, run: `npm install`
Once all the dependencies are installed, run: `npm start`

This will open the frontend of the website at: `http://localhost:3000`

You can explore the application from there. 

### API Reference

#### Getting Started

* The API will run on: `http://localhost:5000` 
* There is no authentication required for any routes. 

#### Error Handling

Errors are returned as JSON objects in the following format, for example: 

```
{
    "success": false,
    "error": 404,
    "message": "resource not found"
}
```

The API currently incporporates the following error types: 

* 400: Bad Request
* 404: Resource Not Found
* 422: Not Processable
* 500: Internal Server Error

#### Endpoints

##### All

* GET /
* GET /categories
* GET /categories/:id
* GET /categories/:id/questions
* GET /questions
* GET /questions?page=2
* GET /questions/:id
* POST /questions
* POST /questions (for search)
* POST /quizzes
* DELETE /questions/:id

##### GET /

###### General

* A sanity check/ping route to check whether the API is running.
* Sample: curl http://localhost:5000/
* HTTP Code: 200
* Response:  

```
{
    "success": false,
    "error": 404,
    "message": "resource not found"
}
```

##### GET /categories

###### General

* Returns a list of all categories.
* Sample: curl http://localhost:5000/categories
* HTTP Code: 200
* Response: 

```
{
  "categories": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "success": true,
  "total": 6
}
```

##### GET /categories/:id

###### General

* Retrieve a specific category.
* Sample: curl http://localhost:5000/category/2
* HTTP Code: 200
* Response:  

```
{
  "id": 2,
  "success": true,
  "type": "Art"
}
```

##### GET /categories/:id/questions

###### General

* Retrieves all questions for a specific category.
* Sample: curl http://localhost:5000/categories/2/questions
* HTTP Code: 200
* Response:  

```
{
  "categories": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "current_category": {
    "id": 2,
    "type": "Art"
  },
  "questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "success": true,
  "total_questions": 4
}
```

##### GET /questions

###### General

* Retrieves all questions with optional ?page=int query parameter.
* Sample: curl http://localhost:5000/questions?page=2
* HTTP Code: 200
* Response:  

```
{
  "categories": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "current_category": null,
  "questions": [
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
      "answer": "South Africa",
      "category": 6,
      "difficulty": 1,
      "id": 25,
      "question": "Which country won the 2019 Rugby World Cup?"
    }
  ],
  "success": true,
  "total_questions": 23
}
```

##### GET /questions/:id

###### General

* Retrieves a specific question.
* Sample: curl http://localhost:5000/questions/2
* HTTP Code: 200
* Response:  

```
{
  "question": {
    "answer": "Apollo 13",
    "category": 5,
    "difficulty": 4,
    "id": 2,
    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
  },
  "success": true
}
```

##### Create Question: POST /questions 

###### General

* Create a new question.
* Body: 
```
{
	"question": "Who is Superman's arch enemy?",
	"answer": "Lex Luthor",
	"category": 5,
	"difficulty": 1
}
```
* HTTP Code: 200
* Response:  

```
{
  "created": 31,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 23
}
```

##### Search for Question(s): POST /questions 

###### General

* Search for question(s).
* Body: 
```
{
	"search": "title"
}
```
* HTTP Code: 200
* Response:  

```
{
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ],
  "success": true,
  "total_questions": 2
}
```

##### POST /quizzes

###### General

* Play the trivia game.
* Body: 
```
{
	"previous_questions":[20, 21],
	"quiz_category":{
		"type":"Science","id":1
	}
}
```
* HTTP Code: 200
* Response:  

```
{
  "question": {
    "answer": "Blood",
    "category": 1,
    "difficulty": 4,
    "id": 22,
    "question": "Hematology is a branch of medicine involving the study of what?"
  },
  "success": true
}
```

##### DELETE /questions/:id

###### General

* Delete a specific question.
* HTTP Code: 200
* Response:  
```
{
  "deleted": 31,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 22
}
```

#### Deployment

No deployment required at present.