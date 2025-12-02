def generate_full_name(firstname,lastname,):
    return firstname + ' ' + lastname

def random_user_id(length:int=6)->str:
    import random
    import string
    user_id=string.ascii_letters+string.digits
    return ''.join(random.choice(user_id) for _ in range(length))

def user_id_gen_by_user():
    import random
    import string

    c=int(input('enter number of characters:'))
    n=int(input('enter number of IDs to generate:'))
    
    alphabet=string.ascii_letters+string.digits

    for i in range(n):
        user_id= ''.join(random.choice(alphabet) for _ in range(c))
        print(user_id)
    return user_id_gen_by_user()    

def rgb_color_gen():
    import random
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return(f'rgb({r},{g},{b})')

def list_of_hexa_colors(count:int)->list[str]:
    import string
    import random
    hex_char=string.hexdigits.lower()[:16]
    return '#' +''.join(random.choice(hex_char) for _ in range(6))

def list_of_rgb_colors(count: int)->list[str]:
    return [rgb_color_gen() for _ in range(count)]

def generate_colors(color_type: str, count:int)->list[str]:
    t=color_type.strip().lower()
    if t=='hexa':
        return list_of_hexa_colors(count)
    if t=='rgb':
        return list_of_rgb_colors(count)
    
def shuffle_list(lst:list)->list:
    import random
    copy=lst[:]
    random.shuffle(copy)
    return copy

def unique_number()->list[int]:
    import random
    return random.sample(range(10),7)