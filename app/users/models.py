from dataclasses import dataclass
from typing import Union

@dataclass(kw_only=True)
class User:
    id: Union[int,None]=None
    name: str
    email: str
    password: Union[str,None]=None
    is_active: bool = True
