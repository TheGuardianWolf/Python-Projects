import os
import glob

print("Path to APK?")
apkLocation=str(input())

print("ADB Location?")
adbLocation=str(input())

for file in glob.glob('"'+apkLocation+"\*.apk"+'"'):
    print("Running command "'"'+adbLocation+'"'+' install '+file)
    os.system('"'+adbLocation+'"'+' install '+file)
