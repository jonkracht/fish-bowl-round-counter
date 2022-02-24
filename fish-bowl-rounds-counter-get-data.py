import requests
from bs4 import BeautifulSoup

def getParticipantData(url):
    '''Return participants who competed in a specified event.'''

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    participantData = []

    year = soup.find(class_="tournament-date").text.split()[-1].split('-')[-1] # tournament year

    # Iterate over tables that contain player info and score
    for table in soup.find_all("table", class_="results sticky-enabled"):
        players = table.find_all(class_ = ['even','odd']) # removes table headers

        for player in players:
            playerInfo = []
            playerInfo.append(player.find(class_='player').text)

            # Handle players without PDGA numbers or simply not supplied:
            try:
                playerInfo.append(player.find(class_ = 'pdga-number').text)
            except:
                playerInfo.append('')

            playerInfo.append(year)

            participantData.append(playerInfo)

    return participantData


def saveData(data, filename):
    '''Save data as csv for later analysis.'''

    import csv

    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=",")

        # Write column headers
        writer.writerow(['Name', 'Number', 'Year'])

        # Write main body of data
        writer.writerows(data)

    return


def main():
    '''Main function to count number of times each player has played FISH bowl'''

    # Event numbers; url for the event is then "pdga.com/tour/event/[eventNumbers]"
    eventNumbers = ['14845', '16962', '19576', '25212', '32338', '35566', '40638', '46171', '51988']

    data = []
    for event in eventNumbers:

        print(f'Scraping data for event number {event}.')

        url = 'http://www.pdga.com/tour/event/' + event
        participants = getParticipantData(url)

        data += participants

    # Save data
    save_file_name = 'fish-bowl-rounds-counter-data.csv'
    saveData(data, save_file_name)


if __name__ == '__main__':
    main()