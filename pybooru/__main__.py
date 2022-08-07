from aiohttp import request
from pybooru import Danbooru

client = Danbooru('danbooru')
artists = client.artist_list('aasu')

for artist in artists:
    print("Name: {0}".format(artist['name']))

def get_images():
    for artist in artists:
        images = client.artist_list(artist)
        for image in images:
            print(image['file_url'])

#take image links
#save them to a file
def save_images():
    for artist in artists:
        images = client.artist_list(artist)
        for image in images:
            print(image['file_url'])
            with open(image['file_url'], 'wb') as f:
                f.write(requests.get(image['file_url']).content)


#create function that take as input image url
#and then save it in this folder
def saveImage(url):
    with open(url, 'wb') as f:
        f.write(request.get(url).content)

imgName = "https://cdn.donmai.us/sample/4a/ea/__usada_pekora_don_chan_and_nousagi_hololive_drawn_by_mirukurim__sample-4aea9377f6af613bb89b6e447d8e2fe6.jpg"

#take image name
def take_name():
    name = imgName.split('/')[-1]
    return name

print(take_name())