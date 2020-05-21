# task 1
# task 1
from sys import argv

script_name, work_ours, payments, premium = argv
salary = (int(work_ours)*int(payments))+int(premium)

print("Ваша ЗП составит: ", salary)
