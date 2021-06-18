from tkinter import *
from  tkinter import messagebox as mb
import json

root = Tk()
root.geometry("800x600")
root.title("Quiz")
with open('quiz.json') as f:
    obj = json.load(f)
q = (obj['ques'])
options = (obj['options'])
a = (obj['ans'])


class Quiz:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correto = 0

    def question(self, qn):
        t = Label(root, text=" Seja bem vindo Quiz em Python, Sao Perguntas Simples !", width=60, bg="blue", fg="white", font=("arial", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text="q[qn]", width=60, font=("times", 16, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val  < 4:
            btn = Radiobutton(root, text="", variable=self.opt_selected, value=val + 1, font=("arial", 15))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
             self.opts[val]['text'] = op
             val += 1

    def buttons(self):
        nbutton = Button(root, text="Próximo", command=self.nextbtn, width="10", bg="green", fg="white", font=("arial", 15, "bold"))
        nbutton.place(x=200, y=380)
        quitbutton = Button(root, text="Sair", command=root.destroy, width="10", bg="red", fg="white", font=("arial", 15, "bold"))
        quitbutton.place(x=380, y=380)
       
    def checkans(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True
       
    def nextbtn(self):
        if self.checkans(self.qn):
            self.correto += 1
        self.qn += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        pontuação = int(self.correto / len(q)* 100)
        resultado = "Pontuação: " + str(pontuação) + "%"
        wc = len(q) - self.correto
        correto = "Número de respostas corretas:" + str(self.correto)
        errado = "Número de respostas erradas:" + str(wc)
        mb.showinfo("Resultado","\n".join([resultado, correto, errado]))

quiz=Quiz()
root.mainloop()