"""
Find all process in the system and pring it's process ID and name and Status
"""
import glob

def findall_PIDs(path):
    all_pids = glob.glob(path)
    track_pids = {}

    for ps in all_pids:
        status = open(ps).read().split()

        pid = status[0]
        name = status[1]
        p_stat = status[2]

        if p_stat not in track_pids:
            track_pids[p_stat] = [[pid, name]]
        else:
            track_pids[p_stat] = track_pids[p_stat] + [[pid, name]]


    for pids in track_pids:
        print track_pids[pids]


findall_PIDs("/proc/[0-9]*/stat")

"""
Work on generate process states for all process
"""
