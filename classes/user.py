@dataclass_json
@dataclass
class User:
    '''Class for creating new users'''
    user_name : str
    user_id : int
    # user_discriminator : str
    jokes : List = []