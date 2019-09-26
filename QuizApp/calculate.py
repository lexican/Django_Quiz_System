P = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0]


def answer(question_id, answer):
    question_id = int(question_id) - 1
    P[question_id] = answer


def showresult():
    score = 0
    for i in range(0, 10):
        if P[i] == 1:
            score += 1
    return score
