def get_video_list_by_timedelta(timedelta):
    objs = VideoFile.objects.filter('TODO: implement time intersection logic')


def push_recent_files_to_remote():
    recent = get_video_list_by_timedelta(timedelta)
    push_to_remote(recent)
