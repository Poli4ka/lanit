#imports
import pandas as pd
import numpy as np
import pymorphy2
import re
from spellchecker import SpellChecker
from nltk.stem.snowball import RussianStemmer

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer

from wordcloud import WordCloud

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import sklearn.metrics as sm

from sklearn.decomposition import NMF
from scipy.spatial.distance import cosine
from scipy.spatial.distance import cdist

#считывание
users = pd.read_csv("C:/Users/polina/users.csv", encoding="windows-1251", index_col=0, header=None)\
.rename({1: "Пол"}, axis=1).replace({"РјСѓР¶": '1', "Р¶РµРЅ": '0'})
users.index = users.index.map(str)
questionary = pd.read_json("C:/Users/polina/q.json")
headers = pd.DataFrame(data = questionary["questions"][0]).text

#создание таблицы
ans = pd.DataFrame(columns=["Интересы", "Фильмы", "Книги", "Музыка", "Хобби"])
def append_each(a, to):
    for n in a:
        n = n.strip()
        if n != "":
            if n.find("нет ") == -1:
                to.append(n.replace('"', "").replace(" ", "_"))
spliter_bm = re.compile(r'[;]')
spliter_else = re.compile(r'[;,]')
deleter_bm = re.compile(r'[!()\[\]{}\\<>/?@#$%^*_~\"-.:]')
deleter_else = re.compile(r'[!()\[\]{}\\<>/?@#$%^*_~\:.-]')
for i in questionary["participations"][0]:
    row = [""]*5
    if questionary["participations"][0][i] is not None:
        for q in questionary["participations"][0][i]:
            cell = []
            if q['questionId'] == '1' or q['questionId'] == '2':
                cell = re.split(spliter_bm, re.sub(deleter_bm, '', q['answer'].lower()))
            else:
                cell = re.split(spliter_else, re.sub(deleter_else, '', q['answer'].lower()))
            new_cell = []
            for item in cell:
                if q['questionId'] != '1' and q['questionId'] != '2' and q['questionId'] != '3':
                    items = item.split(' и ')
                    if len(items) == 1:
                        items = item.split('\"\"')
                    append_each(items, new_cell)
                else:
                    append_each([item], new_cell)
            if new_cell:
                row[int(q['questionId'])] = " ".join(new_cell)
    ans.loc[i] = row
#ans[ans['Книги'].str.contains("_", na=False)].head()
ans.loc["3298830"]["Книги"] = "мертвый_инквизитор"
ans.loc["236879340"]["Книги"] = "вдовий_пароход"
ans.loc["1328104819"]["Книги"] = "всепоглощающий_огонь"
ans.loc["52143323"]["Книги"] = "женщины"
ans.loc["106890293"]["Книги"] = "тонкое_искуство_пофигизма"
ans.loc["123686708"]["Книги"] = "биология_добра_и_зла"
ans.loc["128880630"]["Книги"] = "богатый_папа_бедный_папа"
ans.loc["139888107"]["Книги"] = "конец_вечности"
ans.loc["192155422"]["Книги"] = "акулы_из_стали"
ans.loc["195780931"]["Книги"] = "антихрупкость аркада"
ans.loc["204339170"]["Книги"] = "степной_волк"
ans.loc["233347698"]["Книги"] = "в_ту_же_реку"
ans.loc["262874826"]["Книги"] = "стража_стража"
ans.loc["341677518"]["Книги"] = "думай_медленно_решай_быстро"
ans.loc["360700835"]["Книги"] = "потерянные_боги"
ans.loc["406430326"]["Книги"] = "мы"
ans.loc["358799673"]["Книги"] = "первый_закон"
#209077883
#247971637
#378975263
ans.loc["1067845477"]["Фильмы"] = "пророк_моисей_вождьосвободитель"
ans.loc["209077883"]["Фильмы"] = "душа джентльмены"
ans.loc["210993200"]["Фильмы"] = "властелин_колец"
ans.loc["667461959"]["Фильмы"] = np.nan


ans = pd.merge(ans, users, how="left", left_index=True, right_index=True)
ans["Все интересы"] = ans["Интересы"]+" "+ans["Хобби"]
def group_similar(words):
    temp = []
    for word in words:
        if word == "кино":
            temp.append("фильмы")
        elif word == "авто":
            temp.append("автомобили")
        elif word == "фото":
            temp.append("фотография")
        elif word == "книги" or word == "литература":
            temp.append("чтение")
        elif word == "рисовать":
            temp.append("рисование")
        elif word == "танцами":
            temp.append("фильмы")
        elif word == "танцы":
            temp.append("фильмы")
        elif word == "картинг":
            temp.append("гонки")
        elif word == "игры":
            temp.append("компьютерные_игры")
        else:
            temp.append(word)
    temp = list(dict.fromkeys(temp))
    return " ".join(temp)

ans["Все интересы"] = ans["Все интересы"].map(lambda x: group_similar(x.split()))
ans["Кол-во интересов"] = ans["Все интересы"].map(lambda x: len(x.split()))
ans.to_csv("interests.csv")