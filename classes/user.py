from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
# from typing import List

@dataclass_json
@dataclass
class User:
    '''Class for creating new users'''
    user_name : str
    user_id : int
    # user_discriminator : str
    jokes : list = field(default_factory=list)