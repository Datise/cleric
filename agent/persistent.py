import subprocess
import tools

def date_format():
    return "-D '%Y-%m-%dT%H:%M'"

def get_launch_agents():
    files = subprocess.run(["ls", "-la", date_format(), "/Library/LaunchAgents"], check=True, capture_output=True).stdout.decode("utf-8").split("\n")[3:]
    return [file.split(" ")[-1] for file in files if file]

def get_launch_daemons():
    files = subprocess.run(["ls", "-la", date_format(), "/Library/LaunchDaemons"], check=True, capture_output=True).stdout.decode("utf-8").split("\n")[3:]
    ffiles = []
    for file in files:
        if not file:
            continue
        
        file = file.split(" ")        
        ffiles.append({
            'perms': file[0],
            'links': file[3],
            'owner': file[4],
            'group': file[6],
            'size': file[9],
            'last_modified': file[11],
            'name': file[12]
        })
    return ffiles

def get_startup_items():
    files = subprocess.run(["ls", "-la", date_format(), "/Library/StartupItems"], check=True, capture_output=True).stdout.decode("utf-8").split("\n")[3:]
    return [file.split(" ")[-1] for file in files if file]

def Get_Persistent():
    return tools.Flatten([get_launch_agents(), get_launch_daemons(), get_startup_items()])