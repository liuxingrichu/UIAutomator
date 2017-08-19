#_*_coding:UTF-8_*__
import os
#######################
jar_name="Demo"
workspace_path="D:\\Android\\work\\Demo2"
ID="2"
test_name="com.uiautomator.demo2.DemoTest2#testDemo"
devices="-s 5HCAAELV8DMN9D4P"
#######################
print 1
os.system("android create uitest-project -n "+jar_name+" -t "+ID+" -p "+"\""+workspace_path+"\"")
print 2
o=open(workspace_path+"\\build.xml", "rb+")
d=""
for s in o.readlines():
    a=s.replace("help", "build")
    d+=a
o.seek(0)
o.truncate
o.write(d)
o.close()

print 3
os.system("ant -buildfile "+"\""+workspace_path+"\\build.xml"+"\"")

print 4
os.system("adb "+devices+" push "+"\""+workspace_path+"\\bin\\"+jar_name+".jar"+"\""+" /data/local/tmp/")

print 5
os.system("adb "+devices+" shell uiautomator runtest "+jar_name+".jar"+" -c "+test_name)

