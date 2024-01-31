from random import choice
def generate_name_files(len_token):
    GEN_CONST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    new_token = ""
    for _ in range(len_token):
        new_token += choice(GEN_CONST)
    return new_token