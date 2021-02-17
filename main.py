import sys
import requests

username = input('Username: ')

website = requests.get('https://GitHub.com/' + username)
page = website.content.decode('utf-8')

if website.status_code == 404:
    print('User not found')
    sys.exit(1)


def extract_data(tab, tag, tag_end, inc):
    global website
    website = requests.get('https://github.com/' + username + '/?tab=' + tab)
    webpage = website.content.decode('utf-8')

    tag_index = webpage.find(tag)
    if tag_index == -1:
        print('Vacuum.')

    while tag_index != -1:
        end_index = webpage.find(tag_end, tag_index + inc)
        print(' - ' + webpage[tag_index + inc: end_index])
        tag_index = webpage.find(tag, tag_index + 1)


index_bio = page.find('f4"')
if page[index_bio + 5] != 'h':
    end_bio = page.find('<', index_bio + 11)
    print(' - ' + page[index_bio + 12: end_bio])


extract_data('profile', 'Home location:', '"', 15)

print('\nFollowers:')

tag = 'k" data-hovercard-type="user" data-hovercard-url="/users/'
extract_data("followers", tag, "/", 57)

print("\nFollowing:")

tag = 'k" data-hovercard-type="user" data-hovercard-url="/users/'
extract_data('following', tag, "/", 57)