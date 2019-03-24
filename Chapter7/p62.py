import redis
from pprint import pprint

if __name__ == '__main__':
  rd = redis.Redis(host = 'localhost', port = 6379, db = 0)
  jp = []
  for artist in rd.hkeys('artist_area'):
    dc = artist.decode()
    if rd.hget('artist_area', dc) == 'Japan'.encode():
      jp.append(dc)
  pprint(jp)