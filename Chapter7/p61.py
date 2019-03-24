import redis

if __name__ == '__main__':
  rd = redis.Redis(host = 'localhost', port = 6379, db = 0)
  ### sample
  # artist = 'Hachi'
  artist = input()
  print(artist)
  print(rd.hget('artist_area', artist).decode())
