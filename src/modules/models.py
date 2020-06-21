from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


def uuid_factory():
    return str(uuid4())


def now_factory():
    return datetime.now().isoformat()


@dataclass
class Tenet:
    description: str
    frequency: int
    days: int
    id: str = field(default_factory=uuid_factory)


@dataclass
class Achievement:
    tenet_id: str
    achieved: bool = True
    achieved_at: str = field(default_factory=now_factory)
