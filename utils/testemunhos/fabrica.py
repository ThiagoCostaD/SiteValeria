# from inspect import signature
from random import randint
from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_testemunho():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'titulo': fake.sentence(nb_words=6),
        'descricao': fake.sentence(nb_words=12),
        'testemunho': fake.text(3000),
        'data_criacao': fake.date_time(),
        'autor': {
            'primeiro_nome': fake.first_name(),
            'ultimo_nome': fake.last_name(),
        },
        'categoria': {
            'name': fake.word()
        },
        'foto': {
            'url': 'https://loremflickr.com/%s/%s/church,faith,hope' % rand_ratio(),  # noqa: E501
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_testemunho())
