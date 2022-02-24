from sqlalchemy.orm import Session
import models
import schemas
from compute_response import compute_response


def check_request_valid(math_expr):
    math_symbols = ['+', '-', '*', '/', '.']
    # math_expr.strip().replace(' ', '')

    # check if the math_expr starts with '*' or '-' and  ends with math symbols (wrong record)
    if math_expr[-1] in math_symbols or math_expr[0] in math_symbols[2:]:
        return False

    # use this method because we need to get access to the next element in math expression to catch doubles
    for i in range(len(math_expr)):
        if math_expr[i] in math_symbols:
            # check next digit to avoid double symbols like '++', '+-' etc
            if math_expr[i + 1] in math_symbols:
                return False

    # math expression is clean, compute the result and return it
    return True


def get_history(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Calculation).offset(skip).limit(limit).all()


def add_calculation(db: Session, postin: schemas.Postin):
    calc = models.Calculation()
    calc.request = postin.request
    if check_request_valid(postin.request):
        calc.response = str(round(compute_response(postin.request), 3))
        calc.status = 'success'
    else:
        calc.response = ''
        calc.status = 'failed'
    db.add(calc)
    db.commit()

    return {'status': calc.status,
            'result': calc.response}
