from datetime import datetime, timedelta
from time import sleep


LENGTH_SECONDS = 10

USER = 'XXX'
PWD = 'YYY'

RTSP_URL = 'rtsp://IP_ADDR:554/profile2/'

OUT_FILE = 'cam999.mov'

COMMAND_BASE = ('openRTSP -q -D 1 -B 10000000 -b 10000000 -Q -F cam1112'
                ' -d 10 -t -u %s %s %s > %s' % (USER, PWD, RTSP_URL, OUT_FILE))

def date_to_str(date):
    return '_'.join(str(date).split(
                            '.')[:-1]).replace(' ', '__').replace(':', '-')

def record():
    timestamp_start = datetime.now()
    start_str = date_to_str(timestamp_start)
    timestamp_end = timestamp_start + timedelta(seconds=LENGTH_SECONDS)
    end_str = date_to_str(timestamp_end)

    filename = start_str + '___' + end_str
    print(filename)
    sleep(2)

if __name__ == '__main__':
    while True:
        record()
