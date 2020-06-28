import random
import nltk

BOT_CONFIG = {
    'intents': {
        'Hello': {
            'examples': ['Привет', 'Здравствуйте', 'Добрый день', 'Хай'],
            'responses': ['Привет', 'Юзер, здравствуй', 'Добрый день, пользователь']
        },
        'Bye': {
            'examples': ['Пока', 'Досвидания', 'Всего доброго', 'Чао'],
            'responses': ['Пока-пока', 'Юзер, счастливо', 'Чао какао']
        },
    },
    'failure_phrases': ['Я вас на понял хозяин', 'Повторите свое требование']
}


def get_intent(text):
    text = text.lower()
    for intent, value in BOT_CONFIG['intents'].items():
        for example in value['examples']:
            distance = nltk.edit_distance(text, example.lower())
            difference = distance / len(example)
            if difference < 0.4:
                return intent


def answer_by_intent(intent):
    responses = BOT_CONFIG['intents'][intent]['responses']
    return random.choice(responses)


def get_failure_phrases():
    failure_phrases = BOT_CONFIG['failure_phrases']
    return random.choice(failure_phrases)

def bot(text):
    # NLU
    intent = get_intent(text)

    # rules
    if intent:
        return answer_by_intent(intent)
    # generative model
    # TODO

    # answer generation

    # return failure phrase
    return get_failure_phrase()

    return 'txt'
