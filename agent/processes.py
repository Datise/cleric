import subprocess

def procs_to_dict(proc):
    nproc = list(filter(None, proc.split(" ")))
    return { 
        "user": nproc[0],
        "pid": nproc[1],
        "cpu": nproc[2],
        "mem": nproc[3],
        "vsz": nproc[4],
        "rss": nproc[5],
        "tt": nproc[6],
        "stat": nproc[7],
        "started": nproc[8],
        "time": nproc[9],
        "cmd": " ".join(nproc[10:])
    }

def parse_procs(procs):
    procs = procs.split("\n")[1:]
    return [procs_to_dict(proc) for proc in procs if proc]

def get_procs():
    return subprocess.run(["ps", "aux"], check=True, capture_output=True).stdout.decode("utf-8")

def Get_Procs():
    return parse_procs(get_procs())

