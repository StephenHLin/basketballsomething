import csv
from collections import OrderedDict
from operator import itemgetter, attrgetter

file_name = 'data/2021-2022.csv'
sort_category = ['PLAYER', 'POS', 'TEAM', 'GP', 'MPG', 'FGM', 'FG%', 'FTM', 'FT%', '3PM', '3P%', 'PTS', 'DREB', 'OREB', 'TREB', 'AST', 'STL', 'BLK', 'TO', 'DD', 'A/TO']

def load_session():
    #load the session, all its players and teams
    return

def save_session():
    #load the session, all its players and teams
    return

def start():
    RAWdata = readdata(file_name) #load data
    sortby(sort_category[-5],RAWdata) #testing funct

def readdata(filename):
    with open(filename, newline='') as f:
        datadict=OrderedDict()
        datadict = [{k: v for k, v in row.items()} #write to a dict
        for row in csv.DictReader(f, skipinitialspace=True)] #1 liner from above line
        return datadict

def sortby(sort_category,data):
    match sort_category:
        case 'PLAYER':
            print('Sort: PLAYER')
            data.sort(key=lambda x:x['PLAYER']) #sort all keys' values, key is 'player' here
            return data
        case 'POS':
            print('Sort: POS')
            data.sort(key=lambda x:x['POS'])
            return data
        case 'TEAM':
            print('Sort: TEAM')
            data.sort(key=lambda x:x['TEAM'])
            return data
        case 'GP':
            print('Sort: GP')
            data.sort(key=lambda x:x['GP'])
            return data
        case 'MPG':
            print('Sort: MPG')
            data.sort(key=lambda x:x['MPG'])
            return data
        case 'FGM':
            print('Sort: FGM')
            data.sort(key=lambda x:x['FGM'])
            return data
        case 'FG%':
            print('Sort: FG%')
            data.sort(key=lambda x:x['FG%'])
            return data
        case 'FTM':
            print('Sort: FTM')
            data.sort(key=lambda x:x['FTM'])
            return data
        case 'FT%':
            print('Sort: FT%')
            data.sort(key=lambda x:x['FT%'])
            return data
        case '3PM':
            print('Sort: 3PM')
            data.sort(key=lambda x:x['3PM'])
            return data
        case '3P%':
            print('Sort: 3P%')
            data.sort(key=lambda x:x['3P%'])
            return data
        case 'PTS':
            print('Sort: PTS')
            data.sort(key=lambda x:x['PTS'])
            return data
        case 'DREB':
            print('Sort: DREB')
            data.sort(key=lambda x:x['DREB'])
            return data
        case 'OREB':
            print('Sort: OREB')
            data.sort(key=lambda x:x['OREB'])
            return data
        case 'TREB':
            print('Sort: TREB')
            data.sort(key=lambda x:x['TREB'])
            return data
        case 'AST':
            print('Sort: AST')
            data.sort(key=lambda x:x['AST'])
            return data
        case 'STL':
            print('Sort: STL')
            data.sort(key=lambda x:x['STL'])
            return data
        case 'BLK':
            print('Sort: BLK')
            data.sort(key=lambda x:x['BLK'])
            return data
        case 'TO':
            print('Sort: TO')
            data.sort(key=lambda x:x['TO'])
            return data
        case 'DD':
            print('Sort: DD')
            data.sort(key=lambda x:x['DD'])
            return data
        case 'A/TO':
            print('Sort: A/TO')
            data.sort(key=lambda x:x['A/TO'])
            return data
    return
                

if __name__ =='__main__':
    start()