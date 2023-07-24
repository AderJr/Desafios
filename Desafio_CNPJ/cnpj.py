import re
from functools import reduce
from random import randint


def validate(cnpj: str):
    cnpj = original_cnpj = number_cnpj(cnpj)
    if len(cnpj) != 14:
        raise ValueError("CNPJ precisa ter 14 dígitos numéricos!")
    valid_cnpj = remove_lasts_digits(cnpj)
    last_digit = calc_last_digits(valid_cnpj)
    valid_cnpj += last_digit

    return original_cnpj == valid_cnpj


def calc_last_digits(formatted_cnpj: str):
    digits = ''
    for which_digit in range(1, 3):
        cnpj_list = gen_cnpj_list(formatted_cnpj+digits)
        validation_list = gen_validation_list(which_digit)
        product_list = gen_product_list(validation_list, cnpj_list)
        product_itens_sum = reduce_product_list(product_list)
        formula_result = apply_formula(product_itens_sum)
        digits += final_digit(formula_result)
    return digits


def generate():
    # 11.111.111/0001-> initial cnpj // 11 -> final digits
    initial_cnpj = [str(randint(0, 9)) for i in range(8)]
    initial_cnpj = ''.join(initial_cnpj) + '0001'
    final_digits = calc_last_digits(initial_cnpj)
    full_cnpj = str(initial_cnpj) + final_digits
    formatted_cnpj = format_cnpj(full_cnpj)
    return formatted_cnpj


def format_cnpj(cnpj: str):
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'


def number_cnpj(cnpj: str):
    return re.sub(r'[^0-9]', '', cnpj)


def remove_lasts_digits(cnpj: str):
    return cnpj[:-2]


def gen_cnpj_list(cnpj: str):
    return [int(x) for x in cnpj]


def gen_validation_list(digit: int):
    if digit == 1:  # validation list of 1° digit
        validation_string = '543298765432'
        validation_list = [int(x) for x in validation_string]
    else:  # validation list of 2° digit
        validation_string = '6543298765432'
        validation_list = [int(x) for x in validation_string]
    return validation_list


def gen_product_list(validation_list: list, cnpj_list: list):
    return [validation_list[i] * cnpj_list[i] for i in range(len(validation_list))]


def reduce_product_list(product_list: list):
    return reduce(lambda ac, i: ac + i, product_list)


def apply_formula(final_sum: int):
    return 11 - (final_sum % 11)


def final_digit(final_sum: int):
    return str(final_sum) if final_sum <= 9 else '0'
