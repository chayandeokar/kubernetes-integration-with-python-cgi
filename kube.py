#!/usr/bin/python3
import subprocess
import cgi
print("Access-Control-Allow-Origin:*")
print("content-type: text/html")
print()
s=cgi.FieldStorage().getvalue("command")

if "create" in s and "deployment" in s:
    a=s.split(" ")
    b=a[2]
    c=b[5:len(b)]
    d=a[3]
    e=d[6:len(d)]
    output=subprocess.getoutput("sudo kubectl create deployment "+c+ " --image "+ e)

elif "create" in s and "pod" in s:
    a = s.split(" ")
    b=a[2]
    c=b[5:len(b)]
    d=a[3]
    e=d[6:len(d)]
    output=subprocess.getoutput("sudo kubectl run "+c+ " --image "+ e     )

elif "expose" in s and "deployment" in s: 
    a = s.split(" ")
    b=a[2]
    c=b[5:len(b)]
    d=a[3]
    e=d[5:len(d)]
    output=subprocess.getoutput("sudo kubectl expose deployment "+c+ " --port="+e+ " --type=NodePort")

elif "scale" in s and "deployment" in s: 
    a=s.split(" ")
    b=a[2]
    c=b[5:len(b)]
    d=a[3]
    e=d[8:len(d)]
    output=subprocess.getoutput("sudo kubectl scale deployment " +c+ " --replicas="+e)

elif ("delete" in s) and ("pod" in s or "deployment" in s):
    a=s.split(" ")
    if "pod" in s:
        b=a[2]
        c=b[5:len(b)]
        #output=c
        output=subprocess.getoutput("sudo kubectl delete pod "+c)
    elif "deployment" in s: 
        b=a[2]
        c=b[5:len(b)]
        output=subprocess.getoutput("sudo kubectl delete deployment "+c)

elif "destroy" in s and "all" in s:
    output=subprocess.getoutput("sudo kubectl delete all --all")


else:
    output=subprocess.getoutput("sudo " +s)

print("<br><br>")
print("<pre>")
print(output)
print("</pre>")
