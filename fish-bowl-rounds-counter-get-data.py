# Import scraping modules
import requests
from bs4 import BeautifulSoup
import csv


def get_participant_numbers(url):
    '''Return list of PDGA numbers who played event'''

    r = requests.get(url) # pull html from website
    soup = BeautifulSoup(r.text, 'html.parser') # format html

    total_info = []

    for table in soup.find_all("table", class_="results sticky-enabled"):
        player_info = table.find_all(class_ = ['even','odd'])
        for player in player_info:
            info = []
            info.append(player.find(class_='player').text)
            print(player.find(class_='player').text)

            # Handle no PDGA field:
            try:
                info.append(player.find(class_ = 'pdga-number').text)
            except:
                info.append('')
            #print('hi')

            total_info.append(info)

    return total_info


def save_data(data, filename):
    '''Save scraped data to file for later analysis'''

    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=",")

        writer.writerow(['Player Name','PDGA number'])
        writer.writerows(data)

    return


def main():
    '''Main function to count number of times each player has played FISH bowl'''

    # PDGA index of FISH Bowl events; url is "pdga.com/tour/event/[INDEX]"
    fish_bowl_event_ids = ['14845','16962','19576','25212','32338','35566','40638','46171','51988']

    all_rounds=[]
    for i in fish_bowl_event_ids:

        print(f'FISH Bowl with event ID: {i}')

        url = 'http://www.pdga.com/tour/event/'+i
        participant_numbers = get_participant_numbers(url)

        #print(f'For event ID {i}, there were {len(participant_numbers)} players and their numbers were:\n{participant_numbers}')

        all_rounds += participant_numbers

        #print('hi')

    # Save data
    save_file_name = 'fish-bowl-rounds-counter-data.csv'
    save_data(all_rounds, save_file_name)


if __name__ == '__main__':
    main()