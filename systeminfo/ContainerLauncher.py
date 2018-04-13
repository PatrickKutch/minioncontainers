import argparse
import subprocess
import os

def main():
    parser = argparse.ArgumentParser(description='Minion Launcher.')
    parser.add_argument("-o","--oscar",help='specifies the IP:PORT of target Oscar',required=True,type=str)
    parser.add_argument("-n","--namespace", help="Namespace for collectors",required=True,type=str)
    parser.add_argument("-f","--frequency", help="Frequency for collection, default is 2000",type=int)

    args = parser.parse_args()

    parts=args.oscar.split(":")
    oscarIP = parts[0]
    oscarPort = parts[1]
    int(parts[1]) # port should be an int

    frequency="2000"
    if None != args.frequency:
        frequency = args.frequency
    
    envVars=dict(os.environ)
    envVars["OscarIP"]=oscarIP
    envVars["oscarPort"]=oscarPort
    envVars["Namespace"]=args.namespace
    envVars["Frequency"]=str(frequency)
    minionProc = subprocess.Popen(["python", "Minion.py", "-i", "systeminfo.xml"],env=envVars)
    minionProc.wait()
    
if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print("Uncaught app error: " + str(ex))



