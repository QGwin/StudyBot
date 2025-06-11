import sqlite3

conn = sqlite3.connect(r"fitness_db.db", check_same_thread=False)
cur = conn.cursor()

def kb_list():
    data = conn.execute('SELECT DISTINCT name  '
                        'FROM trener_list; '    )
    kb_list=[]
    for i in data:
        kb_list.append(i[0])
    return kb_list

def info_trener(name):
    data = conn.execute('SELECT tg_name, specialty, achievment, exp_years '
                        'FROM trener_list '
                        f'WHERE name="{name}";')
    datalist=[i for i in data]
    text=f'<b>{name}</b> \n'\
         f'Телеграмм: <em>{datalist[0][0]}</em> \n' \
         f'Специальность:    <em>{datalist[0][1]}</em> \n' \
         f'Достижения:    <em>{datalist[0][2]}</em> \n' \
         f'Тренерский стаж (в годах):    <em>{datalist[0][3]}</em> \n\n' \
         'Можете записать на тренировку на нашем сайте!'
    return text
var="""id

mes"""
varlist=var.split('\n\n')
print(varlist)