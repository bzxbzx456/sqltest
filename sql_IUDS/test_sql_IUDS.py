import pymysql
from sql_IUDS import HeroDB
from settings import dbparams


def main():
    conn = pymysql.connect(**dbparams)
    # conn = pymysql.connect(host='localhost', user='root', passwd='4866098', db='homework_student', port=3306, charset='utf8')
    cur = conn.cursor()

    # ------------------------------------------- create -----------------------------------------------------
    hero = HeroDB('hero', conn, cur)
    hero.createTable('heros')


    # ------------------------------------------- insert -----------------------------------------------------
    hero.insert('heros', [3, 'Prophet', 0, 2000, 'The hero who in fairy tale.'])

    # ------------------------------------------- select -----------------------------------------------------

    'first record'
    result = hero.selectFirst('heros')
    print(result)
    print("*"*100)

    'last record'
    result = hero.selectLast('heros')
    print(result)
    print("*" * 100)

    'more record'
    results = hero.selectNRecord('heros', 3)
    for item in results:
        print(item)
    print("*" * 100)

    'all record'
    results = hero.selectAll('heros')
    for item in results:
        print(item)
    print("*" * 100)
    # ------------------------------------------- update -----------------------------------------------------
    hero.updateSingle('heros', ['Zeus', 1, 22000, 'The god.', 2])

    values = []
    values.append(['SunWukong', 1, 1300, 'The hero who in fairy tale.', 1])
    values.append(['Zeus', 1, 50000, 'The king who in The Quartet myth.', 2])
    values.append(['Prophet', 1, 20000, 'The hero who in fairy tale.3', 3])
    hero.update('heros', values)

    # ------------------------------------------- delete -----------------------------------------------------
    # hero.deleteByID('heros', 1)
    #
    # hero.dropTable('heros')
    #
    # hero.dropDB('hero')


if __name__ == '__main__':
    main()