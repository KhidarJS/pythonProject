
import random
import nltk
BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['Привет', 'Добрый день', 'Добрый вечер', 'Шалом', 'Приветики', 'Здравствуйте'],
            'responses': ['Привет, человек!', 'Здравствуйте']
        },
        'bye': {
            'examples': ['Пока', 'Досвидания', 'До свидания', 'Прощайте', 'Чао'],
            'responses': ['Еще увидимся', 'Если что, я тут']
        },
    },
    'failure_phrases': [
        "Не понятною. Перефразируйте пожалйста",
        "Я еще только учусь. Не умею на такое отвечать",
    ],
}
def clear_text(text):
    text = text.lower()
    text = ''.join(char for char in text if char in 'абвгдеёжзийклмнопрстуфхцчшщъьыюя -')
    return text
def classify_intent(replica):
    replica = clear_text(replica)

    for intent, intent_data in BOT_CONFIG['intents']:
        for example in intent_data['examples']:
            example = clear_text(example)

            distance = nltk.edit_distance(replica, example) #редакционое расстояние для сравнения слов по смылу
            if distance / len(example) < 0.3:
                return intent
    return 'hello'
def get_answer_by_intent(intent):
    if intent in BOT_CONFIG['intents']:
        responses = BOT_CONFIG['intents'][intent]['responses']
        return random.choice(responses)
def generate_answer(replica):
    #TODO
    return
def get_stub():
    failure_phrases = BOT_CONFIG['failure_phrases']
    return random.choice(failure_phrases) #случайный выбор из фраз

def bot(replica):
    #NLU
    intent = classify_intent(replica)

    # получение Ответа

    # правила
    if intent:
        answer = get_answer_by_intent(intent)
        if answer:
            return answer

    # генеративная модель
    answer = generate_answer(replica)
    if answer:
        return answer

    # заглушка
    answer = get_stub()
    return answer

print(bot('Привет'))