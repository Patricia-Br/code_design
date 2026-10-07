from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandlerError1:
  def variance(self, numbers: List[float]) -> float:
    return 3

class MockDriverHandlerError2:
  def variance(self, numbers: List[float]) -> float:
    return 1000000

# variância muito MENOR do que multiplicação dos valores de numbers
def test_calculate_with_variance_error():
  mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5] })
  calculator_3 = Calculator3(MockDriverHandlerError1())

  with raises(Exception) as excinfo:
    calculator_3.calculate(mock_request)

  assert str(excinfo.value) == 'Falha no processo: Variância menor que multiplicação'

# variância muito MAIOR do que multiplicação dos valores de numbers
def test_calculate():
  mock_request = MockRequest({ "numbers": [1, 1, 1, 1, 100] })
  calculator_3 = Calculator3(MockDriverHandlerError2())

  response = calculator_3.calculate(mock_request)

  assert response == {'data': {'Calculator': 3, 'value': 1000000, 'Success': True}}


