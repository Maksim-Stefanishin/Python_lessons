# Напишите рекурсивную программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 

# 2+2 => 4; 

# 1+2*3 => 7; 

# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:* 


#     1+2*3 => 7; 

#     (1+2)*3 => 9;
# Тут может помочь библиотека re


# import re

# def calculate(expression):
#         pattern = r'^[0-9()+\-*/^\s]+$'
#         if bool(re.match(pattern, expression)):
#                 return eval(expression)
#         else:
#                 return 'Error'

# print(calculate("22^3"))
# print(calculate("1+2*3"))
# print(calculate("1-2*3"))
# print(calculate("(((1+2)*3)+345*89*(23+(45-7*8)))*34"))
# print(calculate(input('Введите арифметического выражения : ')))



# from pythonds.basic.stack import Stack
# from pythonds.trees.binaryTree import BinaryTree

# def buildParseTree(fpexp):
#     fplist = fpexp.split()
#     pStack = Stack()
#     eTree = BinaryTree('')
#     pStack.push(eTree)
#     currentTree = eTree
#     for i in fplist:
#         if i == '(':
#             currentTree.insertLeft('')
#             pStack.push(currentTree)
#             currentTree = currentTree.getLeftChild()
#         elif i not in ['+', '-', '*', '/', ')']:
#             currentTree.setRootVal(int(i))
#             parent = pStack.pop()
#             currentTree = parent
#         elif i in ['+', '-', '*', '/']:
#             currentTree.setRootVal(i)
#             currentTree.insertRight('')
#             pStack.push(currentTree)
#             currentTree = currentTree.getRightChild()
#         elif i == ')':
#             currentTree = pStack.pop()
#         else:
#             raise ValueError
#     return eTree

# pt = buildParseTree("( ( 10 + 5 ) * 3 )")
# pt.postorder()  #определено и объясняется в следующем разделе