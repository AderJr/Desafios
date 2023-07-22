import re
from functools import reduce


def validate(cnpj: str):
    cnpj = format_cnpj(cnpj)
    original_cnpj = cnpj
    cnpj = remove_lasts_digits(cnpj)
    while len(cnpj) < 14:
        cnpj_list = gen_cnpj_list(cnpj)
        validation_list = gen_validation_list(cnpj)
        product_list = gen_product_list(validation_list, cnpj_list)
        final_sum = reduce_product_list(product_list)
        formula_result = apply_formula(final_sum)
        cnpj = add_final_digit(cnpj, formula_result)
    is_valid_ = is_valid(original_cnpj, cnpj)
    return is_valid_


def format_cnpj(cnpj: str):
    return re.sub(r'[^0-9]', '', cnpj)


def remove_lasts_digits(cnpj: str):
    return cnpj[:-2]


def gen_cnpj_list(cnpj: str):
    return [int(x) for x in cnpj]


def gen_validation_list(cnpj: str):
    if len(cnpj) == 12:
        validation_string = '543298765432'
        validation_list = [int(x) for x in validation_string]
    elif len(cnpj) == 13:
        validation_string = '6543298765432'
        validation_list = [int(x) for x in validation_string]
    return validation_list


def gen_product_list(validation_list: list, cnpj_list: list):
    product_list = [validation_list[i] * cnpj_list[i] for i in range(len(cnpj_list))]
    return product_list


def reduce_product_list(product_list: list):
    return reduce(lambda ac, i: ac + i, product_list)


def apply_formula(final_sum: int):
    return 11 - (final_sum % 11)


def add_final_digit(cnpj: str, final_sum: int):
    if final_sum > 9:
        cnpj += '0'
    else:
        cnpj += str(final_sum)
    return cnpj


def is_valid(original_cnpj: str, cnpj: str):
    if original_cnpj == cnpj:
        return True
    else:
        return False
