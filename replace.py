import os
import re
import sys

input_file: str = sys.argv[1]
value_XXX = float(sys.argv[2])
value_XXX_str = "{0:.3f}".format(value_XXX)
value_YYY: float = value_XXX / (3 ** 0.5)
output_file = "kkr.in"

with open(input_file, mode='r', encoding='utf-8') as in_f:
    body = in_f.read()
    body = re.sub('XXX', value_XXX_str, body)
    body = re.sub('YYY', "{0:.8f}".format(value_YYY), body)

new_dir_path = "./{0}".format(value_XXX_str)
os.makedirs(new_dir_path)

with open(new_dir_path + "/" + output_file, mode='w', encoding='utf-8') as out_f:
    out_f.write(body)

