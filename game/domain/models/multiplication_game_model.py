class MultiplicationGameModel:
    def __init__(
        self,
        user_id: int,
        class_id: int,
        multiplication_table: int,
        round: int,
        errors: int,
    ) -> None:
        self.user_id = user_id
        self.class_id = class_id
        self.multiplication_table = multiplication_table
        self.round = round
        self.errors = errors
