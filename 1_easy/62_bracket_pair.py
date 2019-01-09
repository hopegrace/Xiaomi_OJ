# description:我们知道，在逻辑表达式中广泛使用了括号，而括号都是层次化成对出现的。也就是任意左括号都应该存在一个在同一逻辑层级的右括号作为对应。
#             现在我们有一些仅由括号组成的字符串序列，保证每个字符为大括号”{”,”}”、中括号”[”,”]”和小括号”(”,”)”中的一种。
#             需要判断给定的的序列是否合法。
# example: input:({[])}  (一行仅由括号组成的字符串)
#          output:0 (如果序列合法输出 1，否则输出 0)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
   stack=[]
   for item in line:
       if item=='{' or item=='[' or item=='(':
           stack.append(item)
       elif item=='}' or item==']' or item==')':
           if len(stack)==0:
               return 0
           elif item == '}' and stack[-1] == '{':
               stack.pop()
           elif item == ']' and stack[-1] == '[':
               stack.pop()
           elif item == ')' and stack[-1] == '(':
               stack.pop()
           else:
               return 0
   return 1


