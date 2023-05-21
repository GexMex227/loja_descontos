print('Bem vindo ao atacado do Guilherme Araujo Vicente')
p_value = float(input('Entre com o valor do produto: '))
quantidade = float(input('Entre com a quantidade do produto: '))


s_desconto = p_value * quantidade
print('O valor sem desconto foi: R$ {:.2f}'.format(s_desconto))

if(quantidade == 10 or quantidade <= 99):
    v_d = 5/100
    desconto = s_desconto * 5 / 100
elif(quantidade == 100 or quantidade <= 999):
    v_d = 10 / 100
    desconto = s_desconto * 10 / 100
elif(quantidade >= 1000):
    v_d = 15 / 100
    desconto = s_desconto * 15 / 100
else:
    print('Erro')


print('O valor com desconto foi: R$ {:.2f}'.format(s_desconto - desconto), '(Desconto de: {}%)'.format(v_d*100))
