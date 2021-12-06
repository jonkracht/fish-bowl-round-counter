import csv
import pandas as pd

def load_data(file_name):
    '''Load saved data (in csv form) into a Pandas dataframe.'''
    return pd.read_csv(file_name)



def main():
    file_name = 'fish-bowl-rounds-counter-data.csv'

    # Load saved data
    data = load_data(file_name)

    print(data.value_counts().head(50))
    #print(data['Player Name'].value_counts().head(20))

    print('hi')

if __name__ == '__main__':
    main()