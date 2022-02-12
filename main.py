from solver import Solver


if __name__ == '__main__':
    answers = {
        'raise': '00002',
        'forte': '00002',
        'judge': '01002',
        'argue': '00012',
        'uncle': '10012',
    }

    s = Solver()
    s.solve(answers)
