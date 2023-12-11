from collections import defaultdict

class Result:
    def __init__(self, user_id: int, class_id: int, multiplication_table: int, round: int, errors: int):
        self.user_id = user_id
        self.class_id = class_id
        self.multiplication_table = multiplication_table
        self.round = round
        self.errors = errors

    def __repr__(self):
        return f'''\nmultiplication_table: {self.multiplication_table}, round: {self.round}, errors: {self.errors}'''

r_1 = Result(1, 1, 1, 1, 2)
r_2 = Result(1, 1, 2, 1, 4)
r_3 = Result(1, 1, 3, 1, 5)
r_4 = Result(1, 1, 1, 2, 4)
r_5 = Result(1, 1, 2, 2, 6)
r_6 = Result(1, 1, 3, 2, 3)

rs = [r_1, r_2, r_3, r_4, r_5, r_6]

round_results = defaultdict(list)

for r in rs:
    round_results[r.round].append({"table": r.multiplication_table, "errors": r.errors})

for round_num, results in round_results.items():
    sum_of_round_errors = sum(result["errors"] for result in results)
    result = {
        "round": round_num,
        "sum_of_round_errors": sum_of_round_errors,
        "resultsRounds": results}
    print(result)