input1 = input()
input2 = input()

values1 = input1.split()
values2 = input2.split()

output = int(values1[1])*float(values1[2]) + int(values2[1])*float(values2[2])

formatted_output = "{:.2f}".format(output)

print("VALOR A PAGAR: R$ ", formatted_output)
