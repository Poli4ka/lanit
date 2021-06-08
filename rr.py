from tkinter import *
import random       
#####################################################################################
def close(event):
        global Ano1
        Ano1.destroy()
def nex(event):
        global Ano1
        Ano1.destroy()
        Ano(event)        
def save (event):
        global var
        global rad01
        global rad02
        global rad03 
        global rad0
        global rad1
        global rad2                 
        global capital
        global Ano1
        global butconf
        if rad01==capital and var.get()==0:
                lab = Label(Ano1, text="Правильно")
                lab.pack()
        elif rad02==capital and var.get()==1:
                lab = Label(Ano1, text="Правильно")
                lab.pack() 
        elif rad03==capital and var.get()==2:
                lab = Label(Ano1, text="Правильно")
                lab.pack()  
        else:
                lab = Label(Ano1, text="Неправильно")
                lab.pack() 
                lab1 = Label(Ano1, text="Правильный ответ:"+capital)
                lab1.pack()
        rad0.configure(state=DISABLED)
        rad1.configure(state=DISABLED)
        rad2.configure(state=DISABLED)
        butconf.configure(state=DISABLED)
        
def Ano (event):
        global Ano1
        Ano1=Toplevel(main)
        Ano1.geometry("400x300") 
        
        y=["Баикири", "Фунафути","Нукуалофа","Порт-Морсби", "Хониара", "Сува", "Порт-Вила", "Нумеа","Паликир","Маджуро", "Хагатна", "Сайпан", "Апиа", "Паго-Паго", "Папеэте", "Аваруа", "Гонолулу"]
        z = [["Кирибати", "Баирики"], ["Cамоа", "Апиа"], ["Тувалу", "Фунафути"],["Папуа-Новая Гвинея", "Порт-Морсби"],[ "Фиджи", "Cува"], ["Соломоновы о-ва","Хониара"],["Вануату", "Порт-Вила"],["Новая Каледония", "Нумеа"], ["Норфолк" , "Кингстон"],[" Федеративные штаты Микронезии","Паликир"], ["Маршалловы острова", "Маджуро"],[ "Науру", "Нет столицы"], ["Гуам", "Хагатна"], ["Содружество Северных Марианских о-вов", "Сайпан"], ["Тонга","Нукуалофа"], [" Новая Зеландия","Веллингтон"], ["Гавайские о-ва","Гонолулу"], ["о-ва Кука","Аваруа"], ["Французская Полинезия","Папеэте"], ["Американские Самоа", "Паго-Паго"]] 
        global capital
        country, capital = random.choice(z)
        z[0][1]
        lab = Label(Ano1, text=country)
        lab.pack()    
        a=random.choice(y)
        b=random.choice(y)
        while a==capital:
                a=random.choice(y)                
        while b==a or b==capital:
                b=random.choice(y)
                
        global rad01
        global rad02
        global rad03 
        global rad0
        global rad1
        global rad2         
        
        ab3=[a,b,capital]                
        rad01=random.choice(ab3)
        rad02=random.choice(ab3)
        rad03=random.choice(ab3)
        while rad02==rad01:
                rad02=random.choice(ab3)  
        while rad03==rad02 or rad03==rad01:
                rad03=random.choice(ab3) 
            
        global var
        var=IntVar()
        var.set(0)
        rad0 = Radiobutton(Ano1, text=rad01,
                  variable=var,value=0)
        rad1 = Radiobutton(Ano1, text=rad02,
                  variable=var,value=1)
        rad2 = Radiobutton(Ano1, text=rad03,
                  variable=var,value=2)   
        rad0.pack()
        rad1.pack()
        rad2.pack()
        
        global butconf
        butconf = Button(Ano1,text="Проверить") 
        butconf.bind("<Button-1>", save)
        butconf.pack()
        
        butclose = Button(Ano1,text="Закончить тест") 
        butclose.bind("<Button-1>", close)
        butclose.pack(side=BOTTOM)
  
        butnext = Button(Ano1,text="Следующий вопрос") 
        butnext.bind("<Button-1>", nex)
        butnext.pack(side=BOTTOM)        
        
######################################################################################################
def close1(event):
        global SouA1
        SouA1.destroy()
def nex1(event):
        global SouA1
        SouA1.destroy()
        SouA(event)        
def save1 (event):
        global var
        global rad01
        global rad02
        global rad03 
        global rad0
        global rad1
        global rad2                 
        global capital
        global SouA1
        if rad01==capital and var.get()==0:
                lab = Label(SouA1, text="Правильно")
                lab.pack() 
        elif rad02==capital and var.get()==1:
                lab = Label(SouA1, text="Правильно")
                lab.pack() 
        elif rad03==capital and var.get()==2:
                lab = Label(SouA1, text="Правильно")
                lab.pack() 
        else:
                lab = Label(SouA1, text="Неправильно")
                lab.pack() 
                lab1 = Label(SouA1, text="Правильный ответ:"+capital)
                lab1.pack()
        global butconf
        rad0.configure(state=DISABLED)
        rad1.configure(state=DISABLED)
        rad2.configure(state=DISABLED)
        butconf.configure(state=DISABLED)
        
        
def SouA (event):
        global SouA1
        SouA1=Toplevel(main)
        SouA1.geometry("400x300") 
        
        y=["Буэнос-Айрос", "Кайена","Бразилиа","Джорджтаун", "Асуньсьон", "Ла-Пас", "Кито", "Парамарибо","Каракас","Лима", "Сантьяго", "Санта-фе-де Богота", "Монтевидео"]
        z = [["Аргентина", "Буэнос-Айрес"], ["Французская Гвиана", "Кайена"], ["Бразилия", "Бразилиа"],["Гайна", "Джорджтаун"],[ "Парагвай", "Асуньсьон"], ["Боливия","Ла-Пас"],["Эквадор", "Кито"], ["Суринам" , "Парамарибо"],["Венесуэлла","Каракас"], ["Перу", "Лима"],[ "Чили", "Сантьяго"], ["Колумбия", "Санта-фе-де Богота"], ["Уругвай", "Монтевидео"]] 
        global capital
        country, capital = random.choice(z)
        z[0][1]
        lab = Label(SouA1, text=country)
        lab.pack()    
        a=random.choice(y)
        b=random.choice(y)
        while a==capital:
                a=random.choice(y)                
        while b==a or b==capital:
                b=random.choice(y)
                
        global rad01
        global rad02
        global rad03 
        global rad0
        global rad1
        global rad2         
        
        ab3=[a,b,capital]                
        rad01=random.choice(ab3)
        rad02=random.choice(ab3)
        rad03=random.choice(ab3)
        while rad02==rad01:
                rad02=random.choice(ab3)  
        while rad03==rad02 or rad03==rad01:
                rad03=random.choice(ab3) 
            
        global var
        var=IntVar()
        var.set(0)
        rad0 = Radiobutton(SouA1, text=rad01,
                  variable=var,value=0)
        rad1 = Radiobutton(SouA1, text=rad02,
                  variable=var,value=1)
        rad2 = Radiobutton(SouA1, text=rad03,
                  variable=var,value=2)   
        rad0.pack()
        rad1.pack()
        rad2.pack()
        
        global butconf
        butconf = Button(SouA1,text="Проверить") 
        butconf.bind("<Button-1>", save1)
        butconf.pack()
        
        butclose = Button(SouA1,text="Закончить тест") 
        butclose.bind("<Button-1>", close1)
        butclose.pack(side=BOTTOM)
  
        butnext = Button(SouA1,text="Следующий вопрос") 
        butnext.bind("<Button-1>", nex1)
        butnext.pack(side=BOTTOM)      
###################################################################
def close2(event):
        global NouA1
        NouA1.destroy()
def nex2(event):
        global NouA1
        NouA1.destroy()
        NouA(event)        
def save2 (event):
        global var
        global rad01
        global rad02
        global rad03 
        global rad0
        global rad1
        global rad2                 
        global capital
        global NouA1
        if rad01==capital and var.get()==0:
                lab = Label(NouA1, text="Правильно")
                lab.pack() 
        elif rad02==capital and var.get()==1:
                lab = Label(NouA1, text="Правильно")
                lab.pack() 
        elif rad03==capital and var.get()==2:
                lab = Label(NouA1, text="Правильно")
                lab.pack() 
        else:
                lab = Label(NouA1, text="Неправильно")
                lab.pack() 
                lab1 = Label(NouA1, text="Правильный ответ:"+capital)
                lab1.pack()
        global butconf
        rad0.configure(state=DISABLED)
        rad1.configure(state=DISABLED)
        rad2.configure(state=DISABLED)
        butconf.configure(state=DISABLED)
def NouA (event):
        global NouA1
        NouA1=Toplevel(main)
        NouA1.geometry("400x300") 
    
        y=["Буэнос-Айрос", "Кайена","Бразилиа","Джорджтаун", "Асуньсьон", "Ла-Пас", "Кито", "Парамарибо","Каракас","Лима", "Сантьяго", "Санта-фе-де Богота", "Монтевидео"]
        z = [["Аргентина", "Буэнос-Айрес"], ["Французская Гвиана", "Кайена"], ["Бразилия", "Бразилиа"],["Гайна", "Джорджтаун"],[ "Парагвай", "Асуньсьон"], ["Боливия","Ла-Пас"],["Эквадор", "Кито"], ["Суринам" , "Парамарибо"],["Венесуэлла","Каракас"], ["Перу", "Лима"],[ "Чили", "Сантьяго"], ["Колумбия", "Санта-фе-де Богота"], ["Уругвай", "Монтевидео"]] 
        global capital
        country, capital = random.choice(z)
        z[0][1]
        lab = Label(NouA1, text=country)
        lab.pack()    
        a=random.choice(y)
        b=random.choice(y)
        while a==capital:
                a=random.choice(y)                
        while b==a or b==capital:
                b=random.choice(y)
                
        global rad01
        global rad02
        global rad03 
        global rad0
        global rad1
        global rad2         
        
        ab3=[a,b,capital]                
        rad01=random.choice(ab3)
        rad02=random.choice(ab3)
        rad03=random.choice(ab3)
        while rad02==rad01:
                rad02=random.choice(ab3)  
        while rad03==rad02 or rad03==rad01:
                rad03=random.choice(ab3) 
            
        global var
        var=IntVar()
        var.set(0)
        rad0 = Radiobutton(NouA1, text=rad01,
                  variable=var,value=0)
        rad1 = Radiobutton(NouA1, text=rad02,
                  variable=var,value=1)
        rad2 = Radiobutton(NouA1, text=rad03,
                  variable=var,value=2)   
        rad0.pack()
        rad1.pack()
        rad2.pack()
        
        global butconf
        butconf = Button(NouA1,text="Проверить") 
        butconf.bind("<Button-1>", save2)
        butconf.pack()
        
        butclose = Button(NouA1,text="Закончить тест") 
        butclose.bind("<Button-1>", close2)
        butclose.pack(side=BOTTOM)
    
        butnext = Button(NouA1,text="Следующий вопрос") 
        butnext.bind("<Button-1>", nex2)
        butnext.pack(side=BOTTOM)   
################################################################
def close3(event):
        global Af1
        Af1.destroy()
def nex3(event):
        global Af1
        Af1.destroy()
        Af(event)        
def save3 (event):
        global var
        global rad01
        global rad02
        global rad03 
        global rad0
        global rad1
        global rad2                 
        global capital
        global Af1
        if rad01==capital and var.get()==0:
                lab = Label(Af1, text="Правильно")
                lab.pack() 
        elif rad02==capital and var.get()==1:
                lab = Label(Af1, text="Правильно")
                lab.pack() 
        elif rad03==capital and var.get()==2:
                lab = Label(Af1, text="Правильно")
                lab.pack() 
        else:
                lab = Label(Af1, text="Неправильно")
                lab.pack() 
                lab1 = Label(Af1, text="Правильный ответ:"+capital)
                lab1.pack()
        global butconf
        rad0.configure(state=DISABLED)
        rad1.configure(state=DISABLED)
        rad2.configure(state=DISABLED)
        butconf.configure(state=DISABLED)
def Af (event):
        global Af1
        Af1=Toplevel(main)
        Af1.geometry("400x300") 
    
        y=["Рабат", "Алжир","Триполи","Каир", "Конакри", "Бамако", "Ниамей","Нджамена","Киншаса", "Малабо", "Луанда", "Хартум", "Адис-Аббеба", "Могадишо", "Найроби","Кампала","Мапуту","Претория","Антананариву"]
        z = [["Марокко", "Рабат"], ["Алжир", "Алжир"], ["Египет", "Каир"],["Ливия", "Триполи"],[ "Гвинея", "Конакри"], ["Мали","Бамако"],["Нигер", "Ниамей"], ["Чад" , "Нджамена"],["ДРК","Киншаса"], ["Экваториальная Гвинея", "Малабо"],[ "Ангола", "Луанда"], ["Судан", "Хартум"], ["Эфиопия", "Адис-Аббеба"],["Сомали", "Могадишо"],[ "Кения", "Найроби"], ["Уганда", "Камапала"], ["Мозамбик", "Мапуту"],[ "ЮАР", "Претория"], ["Мадагаскар", "Антананариву"]] 
        global capital
        country, capital = random.choice(z)
        z[0][1]
        lab = Label(Af1, text=country)
        lab.pack()    
        a=random.choice(y)
        b=random.choice(y)
        while a==capital:
                a=random.choice(y)                
        while b==a or b==capital:
                b=random.choice(y)
                
        global rad01
        global rad02
        global rad03 
        global rad0
        global rad1
        global rad2         
        
        ab3=[a,b,capital]                
        rad01=random.choice(ab3)
        rad02=random.choice(ab3)
        rad03=random.choice(ab3)
        while rad02==rad01:
                rad02=random.choice(ab3)  
        while rad03==rad02 or rad03==rad01:
                rad03=random.choice(ab3) 
            
        global var
        var=IntVar()
        var.set(0)
        rad0 = Radiobutton(Af1, text=rad01,
                  variable=var,value=0)
        rad1 = Radiobutton(Af1, text=rad02,
                  variable=var,value=1)
        rad2 = Radiobutton(Af1, text=rad03,
                  variable=var,value=2)   
        rad0.pack()
        rad1.pack()
        rad2.pack()
        
        global butconf
        butconf = Button(Af1,text="Проверить") 
        butconf.bind("<Button-1>", save3)
        butconf.pack()
        
        butclose = Button(Af1,text="Закончить тест") 
        butclose.bind("<Button-1>", close3)
        butclose.pack(side=BOTTOM)
    
        butnext = Button(Af1,text="Следующий вопрос") 
        butnext.bind("<Button-1>", nex3)
        butnext.pack(side=BOTTOM)   
###########################################
def close4(event):
        global E1
        E1.destroy()
def nex4(event):
        global E1
        E1.destroy()
        E(event)        
def save4 (event):
        global var
        global rad01
        global rad02
        global rad03 
        global rad0
        global rad1
        global rad2                 
        global capital
        global E1
        if rad01==capital and var.get()==0:
                lab = Label(E1, text="Правильно")
                lab.pack() 
        elif rad02==capital and var.get()==1:
                lab = Label(E1, text="Правильно")
                lab.pack() 
        elif rad03==capital and var.get()==2:
                lab = Label(E1, text="Правильно")
                lab.pack() 
        else:
                lab = Label(E1, text="Неправильно")
                lab.pack() 
                lab1 = Label(E1, text="Правильный ответ:"+capital)
                lab1.pack()
        global butconf
        rad0.configure(state=DISABLED)
        rad1.configure(state=DISABLED)
        rad2.configure(state=DISABLED)
        butconf.configure(state=DISABLED)
def E (event):
        global E1
        E1=Toplevel(main)
        E1.geometry("400x300") 
    
        y=["Буэнос-Айрос", "Кайена","Бразилиа","Джорджтаун", "Асуньсьон", "Ла-Пас", "Кито", "Парамарибо","Каракас","Лима", "Сантьяго", "Санта-фе-де Богота", "Монтевидео"]
        z = [["Аргентина", "Буэнос-Айрес"], ["Французская Гвиана", "Кайена"], ["Бразилия", "Бразилиа"],["Гайна", "Джорджтаун"],[ "Парагвай", "Асуньсьон"], ["Боливия","Ла-Пас"],["Эквадор", "Кито"], ["Суринам" , "Парамарибо"],["Венесуэлла","Каракас"], ["Перу", "Лима"],[ "Чили", "Сантьяго"], ["Колумбия", "Санта-фе-де Богота"], ["Уругвай", "Монтевидео"]] 
        global capital
        country, capital = random.choice(z)
        z[0][1]
        lab = Label(E1, text=country)
        lab.pack()    
        a=random.choice(y)
        b=random.choice(y)
        while a==capital:
                a=random.choice(y)                
        while b==a or b==capital:
                b=random.choice(y)
                
        global rad01
        global rad02
        global rad03 
        global rad0
        global rad1
        global rad2         
        
        ab3=[a,b,capital]                
        rad01=random.choice(ab3)
        rad02=random.choice(ab3)
        rad03=random.choice(ab3)
        while rad02==rad01:
                rad02=random.choice(ab3)  
        while rad03==rad02 or rad03==rad01:
                rad03=random.choice(ab3) 
            
        global var
        var=IntVar()
        var.set(0)
        rad0 = Radiobutton(E1, text=rad01,
                  variable=var,value=0)
        rad1 = Radiobutton(E1, text=rad02,
                  variable=var,value=1)
        rad2 = Radiobutton(E1, text=rad03,
                  variable=var,value=2)   
        rad0.pack()
        rad1.pack()
        rad2.pack()
        
        global butconf
        butconf = Button(E1,text="Проверить") 
        butconf.bind("<Button-1>", save4)
        butconf.pack()
        
        butclose = Button(E1,text="Закончить тест") 
        butclose.bind("<Button-1>", close4)
        butclose.pack(side=BOTTOM)
    
        butnext = Button(E1,text="Следующий вопрос") 
        butnext.bind("<Button-1>", nex4)
        butnext.pack(side=BOTTOM)   
###########################################################################
def close5(event):
        global A1
        A1.destroy()
def nex5(event):
        global A1
        A1.destroy()
        A(event)        
def save5 (event):
        global var
        global rad01
        global rad02
        global rad03 
        global rad0
        global rad1
        global rad2                 
        global capital
        global A1
        if rad01==capital and var.get()==0:
                lab = Label(A1, text="Правильно")
                lab.pack() 
        elif rad02==capital and var.get()==1:
                lab = Label(A1, text="Правильно")
                lab.pack() 
        elif rad03==capital and var.get()==2:
                lab = Label(A1, text="Правильно")
                lab.pack() 
        else:
                lab = Label(A1, text="Неправильно")
                lab.pack() 
                lab1 = Label(A1, text="Правильный ответ:"+capital)
                lab1.pack()
        global butconf
        rad0.configure(state=DISABLED)
        rad1.configure(state=DISABLED)
        rad2.configure(state=DISABLED)
        butconf.configure(state=DISABLED)
def A (event):
        global A1
        A1=Toplevel(main)
        A1.geometry("400x300") 
    
        y=["Буэнос-Айрос", "Кайена","Бразилиа","Джорджтаун", "Асуньсьон", "Ла-Пас", "Кито", "Парамарибо","Каракас","Лима", "Сантьяго", "Санта-фе-де Богота", "Монтевидео"]
        z = [["Аргентина", "Буэнос-Айрес"], ["Французская Гвиана", "Кайена"], ["Бразилия", "Бразилиа"],["Гайна", "Джорджтаун"],[ "Парагвай", "Асуньсьон"], ["Боливия","Ла-Пас"],["Эквадор", "Кито"], ["Суринам" , "Парамарибо"],["Венесуэлла","Каракас"], ["Перу", "Лима"],[ "Чили", "Сантьяго"], ["Колумбия", "Санта-фе-де Богота"], ["Уругвай", "Монтевидео"]] 
        global capital
        country, capital = random.choice(z)
        z[0][1]
        lab = Label(A1, text=country)
        lab.pack()    
        a=random.choice(y)
        b=random.choice(y)
        while a==capital:
                a=random.choice(y)                
        while b==a or b==capital:
                b=random.choice(y)
                
        global rad01
        global rad02
        global rad03 
        global rad0
        global rad1
        global rad2         
        
        ab3=[a,b,capital]                
        rad01=random.choice(ab3)
        rad02=random.choice(ab3)
        rad03=random.choice(ab3)
        while rad02==rad01:
                rad02=random.choice(ab3)  
        while rad03==rad02 or rad03==rad01:
                rad03=random.choice(ab3) 
            
        global var
        var=IntVar()
        var.set(0)
        rad0 = Radiobutton(A1, text=rad01,
                  variable=var,value=0)
        rad1 = Radiobutton(A1, text=rad02,
                  variable=var,value=1)
        rad2 = Radiobutton(A1, text=rad03,
                  variable=var,value=2)   
        rad0.pack()
        rad1.pack()
        rad2.pack()
        
        global butconf
        butconf = Button(A1,text="Проверить") 
        butconf.bind("<Button-1>", save5)
        butconf.pack()
        
        butclose = Button(A1,text="Закончить тест") 
        butclose.bind("<Button-1>", close5)
        butclose.pack(side=BOTTOM)
    
        butnext = Button(A1,text="Следующий вопрос") 
        butnext.bind("<Button-1>", nex5)
        butnext.pack(side=BOTTOM)   
################################################################
        
main = Tk()
main.geometry("200x200")

but1 = Button(main, 
             text="Австралия и Океания", 
             width=20)
but2 = Button(main,text="Южная Америка", width=20) 
but3 = Button(main,text="Северная Америка", width=20) 
but4 = Button(main,text="Европа", width=20) 
but5 = Button(main,text="Африка",  width=20) 
but6 = Button(main,text="Азия",  width=20) 

but1.pack()
but2.pack()
but3.pack()
but4.pack()
but5.pack()
but6.pack()                    

but1.bind("<Button-1>", Ano )
but2.bind("<Button-1>", SouA )
but3.bind("<Button-1>", NouA )
but4.bind("<Button-1>", E )
but5.bind("<Button-1>", Af )
but6.bind("<Button-1>", A )


main.mainloop()