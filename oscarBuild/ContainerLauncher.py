import argparse
import subprocess
import os

def main():
    parser = argparse.ArgumentParser(description='Minion Launcher.')
    parser.add_argument("-t","--target",help='specifies the IP:PORT of target Oscar or Marvin',required=True,type=str)
    parser.add_argument("-p","--port",help="the UDP port to listen on default is 3232",type=int,default=3232)
    parser.add_argument("-i","--id",help="the Oscar ID, default is 'ContainerizedOscar'",type=str,default="ContainerizedOscar")

    args = parser.parse_args()

    parts=args.target.split(":")
    marvinIP = parts[0]
    marvinPort = parts[1]
    int(parts[1]) # port should be an int
   
    envVars=dict(os.environ)
    envVars["MarvinIP"]=marvinIP
    envVars["MarvinPort"]= marvinPort
    envVars["ListenPort"] = str(args.port)
    
    oscarProc = subprocess.Popen(["python", "Oscar.py", "-i", "OscarConfig.xml"],env=envVars)
    oscarProc.wait()
    
if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print("Uncaught app error: " + str(ex))



