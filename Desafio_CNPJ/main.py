"""
This challenge consists of evaluating a series of cnpj's, using the proper methodology
Methodology: https://www.macoratti.net/alg_cnpj.htm
"""
import cnpj

cnpj_list = ['00.000.000/0001-91', '04.252.011/0001-10', '40.688.134/0001-61', '71.506.168/0001-11', '12.544.992*0001-05']

# for cnpj_i in cnpj_list:
#     resp = cnpj.validate(cnpj_i)
#     if resp:
#         print(f'{cnpj_i} its valid.\n')
#     else:
#         print(f'{cnpj_i} its invalid.\n')

print(cnpj.generate())
