from dataclasses import dataclass
from typing import List, Optional


@dataclass
class IRFunction:
    name: str
    args: List[str]
    return_type: Optional[str]
    body_logic: str
    calls: List[str]
    description: Optional[str]


@dataclass
class IRModule:
    functions: List[IRFunction]
    imports: List[str]
