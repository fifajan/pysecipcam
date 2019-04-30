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

COMMAND_BASE = ('openRTSP '
                '-q -D 1 -B 10000000 -b 10000000 -Q -d 10 -t'
                ' -u %s %s %s' % (USER, PWD, RTSP_URL))

# video data emulation, this outputs 1mb of rand data:
COMMAND_DASE = 'head -c 1M < /dev/urandom'

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
    exec_cmd = COMMAND_BASE.split()[0]
    exec_cmd_args = COMMAND_BASE.split()[1:]
    exec_cmd_args[-1] += filename + OUT_FILE

    # execution:
    with open(filename, 'wb') as out_fl:
        sp.call([exec_cmd] + exec_cmd_args, stdout=out_fl)

    sleep(2)

if __name__ == '__main__':
    while True:
        record()
