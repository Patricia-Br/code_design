from typing import Dict

def add(elem1: int, elem2: float) -> Dict:
  response = elem1 + elem2
  return {"sum": response}

val1 = add(1, 2.34)

print(val1)

#typing: int float, str, bool = True