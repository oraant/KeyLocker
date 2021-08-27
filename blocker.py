from tkinter import *
from random import choices


# ■■■ 说明 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


# 一，修改seconds、content等，将主要内容替换为自己要加密的东西

# 二，使用命令，将其编译为pyd文件：python build_pyd.py build_ext --inplace

# 三，使用命令，将其编译为exe文件：pyinstaller -i icon.ico -Fw blocker_main.py

# 四，使用命令解包，确保pyd优先py被导入：python pyinstxtractor.py dist/blocker_main.exe

# 五，测试生成的程序，放入不同的路径打开，保证没问题，并生成多个不同难度的程序

# 六，在版本管理中，直接用revert删除刚刚的改动，保证了密文只保存在刚才生成的程序中


# ■■■ 配置 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


# 生成任务
puzzle = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' # 生成任务时，随机字符从这里挑选字符出题，用以拦截（不要有'] '，否则会扰乱判断正确答案时的split方法）
length = 10 # 生成任务时，单次生成字符的长度（最终作答时需要反序编写，这是为了防止用OCR识别工具作弊，如有道截屏翻译）
times = 100 # 生成任务时，一共考验多少次（拆成这样也是为了防止用OCR识别工具作弊，如有道截屏翻译）

# 配置解锁内容
content = ['p', 'a', 's', 's', 'w', 'o', 'r', 'd'] # 完成任务后，展示给用户的解锁内容

# 下面的longtxt是赠送的一段 10*5*2*5*2=1000 长度的随机字符，可用作其他密码。若以后想更换，随时可以用下面的代码再生成一次：
# from random import choices; puzzle = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
# print('='*54+'\n'+('\n\n'+'-'*54+'\n\n').join(['\n\n'.join(['\n'.join([' '.join([''.join(choices(puzzle, k=10)) for i in range(5)]) for j in range(2)]) for k in range(5)]) for l in range(2)])+'\n'+'='*54)
longtxt = '''
======================================================
l5hx5QHf6N giz0RW8xKa ljg8JPWw2q wVtIqzikh5 ug7HOckd5P
g23F4qdnFt fGSHGGBrck nvGpiW6iD5 sxMjLAEzb1 BPdl1GWe02

IByMW4hr1U NBNezeDvgU pFRfolBzwU ekca1aG5h5 HUSKYQSkI9
BswfLfKDfS 1WhlbmyQT4 pPZE1CAoaB 5X3UWy2lgj 1fpnG5a26Q

pfgKFzbVy4 R2GGRlqyXD 415Nv6EH4t CYl6PPPyYP kTIMY7X2JB
GCAwFhLCFs FqMU7633g0 m8TAyRPrTl 9MWYQ0iZfm tigs87XK8r

wYb6YPuutM nDxoxY0yJx aiXpMl9xYe yoviDZLLN0 JVylNSoYGm
rbzORa8kvN Obyj4XHylc R82yrAyiF0 mNfRZPFBcW Ker804TqFn

B3ga2rjMju nDbjdRrHdY 3W9nkPVm3q 2Zc5JTIbDT ruVYuSq2SO
gSHWlNthGv kzSbssYFuR joZh3pmjTM ScBYRFEz8o tcT0k64MTf

------------------------------------------------------

zQwQ7JSZro U2cPt1a76i 3vbaungFV0 XDR3BKMQiL whxSmFswWk
1AMPgBbjea rvpAbcueKu Ndqs2ptdXZ z0n56C0Kv0 NPAWTAzUxh

4YRjVPpRlC k6fJKGzSOx qy65QtcuBz kHwS3GVg0l LGdYhEim82
XhEEiXDNPa vehIeWi5hZ q9QpFgBruz Koj5ttUOTz tzlhcV7ywR

YTgY8UgzFv Dc1I9g4weD ZMZ2AlCqyp QvqPzgGsiy c2wDyBQj5J
K0JzfTyPmG BfZGNwjKxJ YjaGoG6jEV uSEeAFERmB HivcVGJHv8

aUBglY0A7O pIJ3PmqH6P xG6j49ikYA eNYeEDnbyU FDveLA5Rs6
s3m2AOfyGi c6mY78s9Aa bIHQcHqrXy eJ7TUUuetJ iQtFlsk5ZZ

lI3TylrU3q xfmZLFFQpR aBJbAf7kJi KMijtUDEVq yudtQsQXiq
tpIle9VxSy jxISurrXlm t4a1pfLUHL zaaFH1qXdK o1lgABnwKK
======================================================
'''


# ■■■ 代码 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


root = Tk()
left = times

def gen_puzzle(): return '[%s/%s] '%(left, times) + ''.join(choices(puzzle, k=length))
def get_puzzle(): return question.cget("text").split('] ')[1][::-1]

def match():
    global left

    if not left: return root.destroy()
    if answer.get()!=get_puzzle(): return button_text.set('错了 重来')

    left -= 1

    if left:
        question_text.set(gen_puzzle())
        button_text.set('对了 继续')
    else:
        question_text.set('解密成功')
        button_text.set('关闭 退出')

        answer_text.set(''.join(content))
        backup_text.set(longtxt.strip())


question_text=StringVar()
question_text.set(gen_puzzle())
question = Label(root, textvariable=question_text, borderwidth=2, relief="groove", font=('consola', 10))
question.grid(row=0, column=0, sticky='nswe', padx=(3,0), pady=3)

answer_text=StringVar()
answer_text.set('')
answer = Entry(root, textvariable=answer_text, borderwidth=2, relief="groove", font=('consola', 10))
answer.grid(row=0, column=1, sticky='nswe', padx=(3,0), pady=3)

button_text=StringVar()
button_text.set('反序 抄写')
button = Button(root, textvariable=button_text, borderwidth=2, relief="groove", font=('consola', 10), command=match)
button.grid(row=0, column=2, sticky='nswe', padx=(3,3), pady=3)

backup_text=StringVar()
backup_text.set('======================================================')
backup = Label(root, textvariable=backup_text, borderwidth=2, relief="groove", font=('consola', 10))
backup.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=3, pady=(0,3))

root.title('信息代价锁 - 非对称决策阻碍装置')
root.resizable(False, False)
def run(): root.mainloop()
