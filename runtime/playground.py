from run import *

for i in range(0, 100):
    p = Parts()
    print(f"Denom: {p.denominator}. First: {p.first_part} - {p.first()}. Second: {p.second_part} - {p.second()}. Second of rem: {p.second_of_remaining} iters: {p.iters}")
