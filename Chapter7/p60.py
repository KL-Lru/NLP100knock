from json import loads
from gzip import open as gzopen
import redis


def get_json():
    ret = []
    with gzopen("artist.json.gz", "rt") as fobj:
        for line in fobj:
            ret.append(loads(line))
    return ret


if __name__ == '__main__':
    rd = redis.Redis(host='localhost', port=6379, db=0)
    datas = get_json()
    for data in datas:
        if 'name' in data and 'area' in data:
            rd.hset('artist_area', data['name'], data['area'])
        elif 'name' in data:
            rd.hset('artist_area', data['name'], 'None')
        elif 'area' in data:
            rd.hset('artist_area', 'None', data['area'])
