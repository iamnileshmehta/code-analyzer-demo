from dataclasses import dataclass
from typing import List, Optional

@dataclass
class KnowledgeObject:
    id: str     #function / class
    type: str
    name: str
    file: str
    code: str

    calls: List[str]
    imports: List[str]

    summary: Optional[str] = None

    