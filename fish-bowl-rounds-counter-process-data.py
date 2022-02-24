import pandas as pd

def load_data(file_name):
    '''Load saved data (in csv form) into a Pandas dataframe.'''
    return pd.read_csv(file_name)



def main():
    '''Clean up data scraped from PDGA.'''

    file_name = 'fish-bowl-rounds-counter-data.csv'

    # Load saved data
    data = load_data(file_name)

    # Make names upper case
    data['Name'] = data['Name'].apply(lambda Name: Name.upper())


    data = data.sort_values(by='Name')


    print(data.value_counts().head(50))
    #print(data['Player Name'].value_counts().head(20))

    print('hi')

if __name__ == '__main__':
    main()