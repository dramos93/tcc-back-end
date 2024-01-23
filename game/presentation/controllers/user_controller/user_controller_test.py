import unittest
from unittest.mock import Mock
from game.presentation.controllers.user_controller.user_controller import CreateUserController

class TestUserController(unittest.TestCase):
    def setUp(self):
        self.use_case = Mock()
        self.auth_use_case = Mock()
        self.user_controller = CreateUserController(self.use_case, self.auth_use_case)

    def test_is_auth_no_permission(self):
        self.auth_use_case.get_user_permissions.return_value = None
        response = self.user_controller.is_auth('dummy_token', [1, 2, 3, 4])
        self.assertEqual(response.body, {"message": "Não autorizado"})
        self.assertEqual(response.status_code, 401)

    def test_is_auth_no_role(self):
        self.auth_use_case.get_user_permissions.return_value = {"user_role": "user"}
        response = self.user_controller.is_auth('dummy_token', [1, 2, 3, 4])
        self.assertEqual(response.body, {"message": "Não autorizado"})
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()