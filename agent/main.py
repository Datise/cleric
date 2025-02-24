import persistent
import processes
import conn

if __name__ == "__main__":
    procs = processes.Get_Procs() 
    persistent_items = persistent.Get_Persistent()
    conn.Send({
        "procs": procs,
        "launch_files": persistent_items
    })
    
    
