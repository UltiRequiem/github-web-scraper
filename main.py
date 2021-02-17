import sys
import requests

username = str(input('GitHub Username: '))

website = requests.get('https://github.com/' + username)

page = website.content.decode('utf-8')

if website.status_code == 404:
    print('User not found.')
    sys.exit(1)


def extract_data(tab, tag, tag_end, inc):  # Don't Delete tab
    tag_index = page.find(tag)
    if tag_index == -1:
        print("This user doesn't have any repository.")

    while tag_index != -1:
        end_index = page.find(tag_end, tag_index + inc)
        print(' - ' + page[tag_index + inc: end_index])
        tag_index = page.find(tag, tag_index + 1)


index_bio = page.find('f4"')
if index_bio == 'h':
    print("This user doesn't have a bio.")  # TODO fix this

elif page[index_bio + 5] != 'hidden':
    endBio = page.find('<', index_bio + 11)
    print(' - ' + page[index_bio + 12: endBio])

extract_data('profile', 'Home location:', '"', 15)
