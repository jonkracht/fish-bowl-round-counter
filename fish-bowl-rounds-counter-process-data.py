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


    data = data.sort_values(by='Number')

    newData = []

    for number in data['Number'].unique():
        matches = data[data['Number'] == number]

        years = sorted(matches['Year'])
        names = list(sorted(matches['Name'].unique()))
        counts = len(years)

        newData.append([names, number, years, counts])


    monkey = pd.DataFrame(newData, columns=['Names', 'Number', 'Years', 'Counts']).sort_values(by='Counts', ascending=False)



    print(data.value_counts().head(50))
    #print(data['Player Name'].value_counts().head(20))

    monkey.to_csv('processed-data.csv')
    print('hi')

if __name__ == '__main__':
    main()