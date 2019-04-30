from datetime import datetime, timedelta
import subprocess as sp
from time import sleep

LENGTH_SECONDS = 10

USER = 'USER'
PWD = 'PASS'

RTSP_URL = 'rtsp://192.168.0.AB:554/profileX/'

OUT_FILE = '_cam999.mov'

# this CLI command works well with Gzr sec camera:
#
# openRTSP -q -D 1 -B 10000000 -b 10000000 -Q -d 10 -t -u <S_LOGIN> 
# <S_PASSWORD> rtsp://192.168.0.ABC:554/profileX/ > vid123.mov

FAKE = True

COMMAND_BASE = ('openRTSP '
                '-q -D 1 -B 10000000 -b 10000000 -Q -d 10 -t'
                ' -u %s %s %s' % (USER, PWD, RTSP_URL))

# video data emulation, this outputs 1mb of rand data:
COMMAND_BASE_FAKE = 'head -c 1M'

def date_to_str(date):
    return '_'.join(str(date).split(
                            '.')[:-1]).replace(' ', '__').replace(':', '-')

def record():
    timestamp_start = datetime.now()
    start_str = date_to_str(timestamp_start)
    timestamp_end = timestamp_start + timedelta(seconds=LENGTH_SECONDS)
    end_str = date_to_str(timestamp_end)

    filename = start_str + '___' + end_str + OUT_FILE

    # execution:
    with open(filename, 'wb') as out_fl:
        if not FAKE:
            sp.call(COMMAND_BASE.split(), stdout=out_fl)
        else:
            with open('/dev/urandom', 'rb') as rand_stream:
                sp.call(COMMAND_BASE_FAKE.split(),
                        stdin=rand_stream, stdout=out_fl)

    sleep(2)

if __name__ == '__main__':
    while True:
        record()
