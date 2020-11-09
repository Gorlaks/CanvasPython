from typing import Dict

def destruct_dict(data: Dict[str, str]) -> str:
  return list(map(lambda x: x[1], sorted(data)))