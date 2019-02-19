import os
import subprocess



# os.system("sudo -S php -v")

# subprocess.call(["sudo", "-S", "php", "-v"])
# subprocess.call(["sudo", "-S", "php", "-i"])
p = subprocess.run(["sudo", "-S", "php", "-i"], stdout=subprocess.PIPE).stdout.decode('utf-8')

# f = open("php.txt","w+")
# f.write(p.stdout.decode('utf-8'))
# f.close()

s = str.find(p, "PHP Version")

p = p[s:s+50]

print(p)


