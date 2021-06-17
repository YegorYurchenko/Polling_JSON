""" Вспомогательные функции """

def delete_empty_variants(variants: str) -> str:
    """ Функция, удаляющая пустые варианты голосования """
    new_variants = variants.split('\n')

    result_variants = []
    for variant in new_variants:
        if len(variant.strip()) > 0:
            result_variants.append(variant.strip())

    return '\n'.join(result_variants)


def get_initial_answers(variants: str) -> str:
    """ Функция, генерирующая начальное состояние ответов голосования """
    amount_of_variants = len(variants.split('\n'))

    return ' '.join(['0' for i in range(amount_of_variants)])

def add_answer_increase(results: list[int], choice_id: int) -> any:
    """ Функция увеличения количества голосов """
    if results and len(results) >= choice_id:
        results[choice_id - 1] += 1
        new_results = list(map(str, results))
        return ' '.join(new_results)

    return None

def split_space_for_result(answers: list[int]) -> list[str]:
    """ Преобразование количества голосов в проценты """
    sum_answers = sum(answers)

    converted_answers = answers
    if sum_answers > 0:
        converted_answers = list(map(lambda x: round((x / sum_answers * 100), 1), answers))

    result = list(map(lambda x: str(x) + '%', converted_answers))
    return result
