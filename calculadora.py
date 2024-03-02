#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import time

opcao = 0

def exibir_menu():
    print('0 : + soma')
    print('1 : - subtracao')
    print('2 : * multiplicacao')
    print('3 : / divisao')
    print('4 : ** exponenciacao')
    

def soma():
    num1 = float(input('Informe o primeiro numero: '))
    num2 = float(input('Informe o segundo numero: '))
    num = float(num1 + num2)
    return print('\n{} + {} = {}'.format(num1, num2, num))

def subtracao():
    num1 = float(input('Informe o primeiro numero: '))
    num2 = float(input('Informe o segundo numero: '))
    num = float(num1 - num2)
    return print('\n{} + {} = {}'.format(num1, num2, num))


def multiplicacao():
    num1 = float(input('Informe o primeiro numero: '))
    num2 = float(input('Informe o segundo numero: '))
    num = float(num1 * num2)
    return print('\n{} * {} = {}'.format(num1, num2, num))

def divisao():
    num1 = float(input('Informe o primeiro numero: '))
    num2 = float(input('Informe o segundo numero: '))
    num = float(num1 / num2)
    return print('\n{} / {} = {}'.format(num1, num2, num))

def exponenciacao():
    num1 = float(input('Informe o primeiro numero: '))
    num2 = float(input('Informe o segundo numero: '))
    num = float(num1 ** num2)
    return print('\n{} ** {} = {}'.format(num1, num2, num))

def main():
    while True:
        os.system('cls')
        exibir_menu()

        opcao = input('\nEscolha a operacao que deseja realizar: ')
        print('=====================================================')

        if opcao == '0':
            soma()
        elif opcao == '1':
            subtracao()
        elif opcao == '2':
            multiplicacao()
        elif opcao == '3':
            divisao()
        elif opcao == '4':
            exponenciacao()
        else:
            print('Opcao invalida. Tente novamente')
            time.sleep(1)
            continue
        print('=====================================================')    
        opcao = input('Voce deseja realizar outra operacao : S / N: ')
        if opcao == 's' or opcao == 'S':
            continue
        else:
            print('Encerrando calculadora')
            break
if opcao == 0:
    main()


# In[ ]:




