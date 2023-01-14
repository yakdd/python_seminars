
pol1 = "2*x**10+3*x**9+2*x**8+3*x**7+1*x**6+2*x**5+3*x**4+3"
pol2 = "6*x**13+3*x**10+2*x**7+1*x**6+2*x**2+3*x**1+10"

pol1 = pol1.split("+")
pol2 = pol2.split("+")

# print(pol1)
# print(pol2)

for indx, value in enumerate(pol1):
    pol1[indx] = list(map(int, (value.split("*x**"))))
print(pol1)


for indx, value in enumerate(pol2):
    pol2[indx] = list(map(int, (value.split("*x**"))))
print(pol2)


result_pol = pol1 + pol2
# print(result_pol)


polyn_dict = {}
for value in result_pol:
    if len(value) > 1:
        if value[1] in polyn_dict.keys():
            polyn_dict[value[1]] += value[0]
        else:
            polyn_dict[value[1]] = value[0]
    else:
        if 0 in polyn_dict.keys():
            polyn_dict[0] += value[0]
        else:
            polyn_dict[0] = value[0]
# print(polyn_dict)


result_pol = dict(sorted(polyn_dict.items(), reverse=True))
print(result_pol)
finish_line = ''
for degree, koeff in result_pol.items():
    if degree > 1:
        finish_line += f"{koeff}*x**{degree} + "
    if degree == 0:
        finish_line += f"{koeff}"

print(finish_line)
