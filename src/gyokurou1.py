#!/usr/bin/python3
import pandas as pd
import itertools

class GameWith:
    def __init__(self, keyword, pages):
        self.uri = lambda page:'https://xn--eckwa2aa3a9c8j8bve9d.gamewith.jp/article/show/' + str(page)
        self.keyword = keyword
        # self.data = self.fetch_page(*pages[0])
        self.data = self.fetch_pages(pages)

    def create_table(self, name, table):
        shaping_row = lambda row: row.translate(str.maketrans({'（':' ','）':''})).split()
        rank = 'Sランク'
        acc = []
        for row in table:
            if row[1] == self.keyword:
                rank = row[0]
                continue
            else:
                acc.append([name, rank, *shaping_row(row[1])])
        return acc

    def fetch_page(self, name, page):
        shaping = lambda s: "".join(s.split('【')[0])
        table = self.create_table(name, pd.read_html(self.uri(page), match = self.keyword)[0].applymap(shaping).values.tolist())
        return pd.DataFrame(data = table, columns = ['対象','ランク', 'モンスター', 'タイプ'])

        

    def fetch_pages(self, pages):
        return pd.concat([self.fetch_page(*page) for page in pages])
    
    def print(self):
        print(self.data)

    def to_csv(self, filename):
        today = pd.to_datetime('today').strftime('%Y%m%d')
        self.data.to_csv('{}.{}.csv'.format(filename, today), index=False)



if __name__ == "__main__":
    pages = (
        ('アヴァロン', 17421)
        , ('ニライカナイ', 21474)
        , ('シャンバラ', 26860)
        , ('エデン', 34072)
        , ('黄泉', 38240)
        , ('ニルヴァーナ',39107)
        , ("ドゥーム", 37345)
        , ('メメントモリ',44088)
        , ('カルマ',45509)
        , ('アカシャ', 46807)
        , ('イザナミ零',21376)
        , ('ヤマトタケル零',28358)
        , ('クシナダ零',23414)
        , ('イザナギ零',21942)
        , ('ツクヨミ零',21943)
        , ('阿修羅',8927)
        , ('毘沙門天',10535)
        , ('摩利支天',12379)
        , ('大黒天', 13704)
        , ('不動明王',15105)
        , ('イザナミ',2339)
        , ('ヤマトタケル',5097)
        , ('クシナダ',4343)
        , ('イザナギ',6062)
        , ('ツクヨミ',7433)
    )

    keyword = 'おすすめ適正ポイント'
    gamewith = GameWith(keyword, pages)
    gamewith.to_csv('gyokurou1')
    
