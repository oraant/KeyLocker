from tkinter import *
import pyperclip
from datetime import datetime as dt


# ■■■ 说明 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


# 一，修改seconds、content等，将主要内容替换为自己要加密的东西

# 二，使用命令，将其编译为pyd文件：python build_pyd.py build_ext --inplace

# 三，使用命令，将其编译为exe文件：pyinstaller -i icon.ico -Fw timer_main.py

# 四，使用python pyinstxtractor.py timer_main.exe 解包，确保pyd优先py被导入

# 五，测试生成的程序，放入不同的路径打开，保证没问题，并生成多个不同难度的程序

# 六，在版本管理中，直接用revert删除刚刚的改动，保证了密文只保存在刚才生成的程序中


# ■■■ 配置 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


seconds = 3 # 等待多久后展示内容
content = ['p', 'a', 's', 's', 'w', 'o', 'r', 'd'] # 等待完毕后，展示给用户的解锁内容（以列表存储，防止反编译/反汇编）
weeks = [1,2,3,4,5,6,7] # 允许使用的星期
begin = '07:00' # 允许使用的开始时间
end = '23:00' # 允许使用的结束时间


# ■■■ 代码 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


def T(string): return dt.strptime(string,'%H:%M').time()

class Window:

    def __init__(self, seconds, content, weeks, begin, end):
        self.seconds = seconds
        self.content = content
        self.weeks   = weeks
        self.begin   = begin
        self.end     = end

        self.root = Tk()
        self.root.title('python信息代价锁 - 非对称决策阻碍装置 - 时间版')
        self.root.resizable(False, False)
        self.root.geometry('300x200')
        self.root.configure(bg="#fefefe")

        self.btn_text=StringVar(); self.btn_text.set('')
        self.btn = Button(self.root, textvariable=self.btn_text, borderwidth=2, width=15, height=2, font=('Microsoft Yahei', 13), command=self.copy, state="disabled")
        self.btn.pack(pady=60)


    def copy(self):
        pyperclip.copy(''.join(self.content))
        self.btn_text.set('复制成功')


    def start(self):
        self.root.after(1, self.check)
        self.root.mainloop()

    def check(self): # 检查星期和时间
        print(T(self.begin) , dt.now().time() , T(self.end))
        print(T(self.begin) < dt.now().time() < T(self.end))
        if dt.now().isoweekday() not in self.weeks: return self.btn_text.set('只有周末可以使用')
        if not T(self.begin) <= dt.now().time() <= T(self.end) : return self.btn_text.set('%s-%s 能用' % (self.begin, self.end))
        self.loop()

    def loop(self): # 倒计时
        if self.seconds == 0: return self.finish()
        self.btn_text.set('剩余%d秒' % self.seconds)
        self.seconds -= 1
        self.root.after(1000, self.loop)

    def finish(self):
        self.btn_text.set('点击复制')
        self.btn.configure(state="normal")

def run():
    Window(seconds, content, weeks, begin, end).start()
