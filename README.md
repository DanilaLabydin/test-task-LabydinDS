# test-task-LabydinDS
this repo contains two tasks(fastapi calculator and tic tac toe game)

1.FastAPI - calculator

requirements: check requirements.txt

Using the Fastape framework, implement a service that calculates the result of an arithmetic expression
and provides an opportunity to view the query history.
There is two enpoints: /calc and /history.

/calc
Takes an arithmetic expression as an input value and outputs either an answer or an error.

the user enters a mathematical expression into a special input form, as a result, an error message and the result of the mathematical expression
or an error message are displayed if the user has entered incorrect characters.the mathematical expression and its result are preserved

the details
user input is checked for validation. valid characters are numbers, spaces, mathematical operands [+-*/().] . If all characters are correct,
the mathematical expression is saved to the database. next, the mathematical expression is calculated (the priority of operations is implemented).
if the mathematical expression is correct, the result will be saved to the database.

/history
The endpoint returns the last 30 (by default) requests to the service in json format (array).

additional parameters: sorting by status and number of records to output

the details
all information from the database is output, it was not possible to limit the internal storage of the database. the data is output in reverse order.

2.Tic tac toe game
the computer plays with itself for two players. At the end of the game, the history of the moves of both "players" and the result are displayed
("Draw", "first player wins", "Second player wins")

the details
the user can set the size of the square playing field. During the implementation process,
I could not add the ability to set the number of consecutive crosses or zeros (diagonals).
