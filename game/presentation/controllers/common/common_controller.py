class CommonController():
        def __init__(
        self, auth_use_case: AuthenticationUserCaseInterface
    ) -> None:
        self.auth = auth_use_case