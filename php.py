import os
import subprocess

class PHP(object):

    positiveRespone = ["yes", "y", "ok", "да", "д"]
    negativeRespone = ["no", "n", "nok", "нет", "н"]
    cmdCurrent = ["sudo", "-S", "php", "-v"]
    phpVersions = ["5.6", "7.0", "7.1", "7.2", "7.3"]
    newVersion = None

    def __init__(self, newVersion = None):
        self.newVersion = None

    def getNewVersion(self):
        wantedVersion = input("Write php version: ")
        if wantedVersion in self.phpVersions:
            self.newVersion = wantedVersion
            return wantedVersion
        else:
            print("Check available version please")
            self.getNewVersion()

    def getCurrentVersion(self):
        phpC = subprocess.run(self.cmdCurrent, stdout=subprocess.PIPE).stdout.decode('utf-8')

        phpCList = phpC.split()

        if phpCList[0].strip() == "PHP":
            return phpCList[1].strip()[:3]  # Cut whitespaces from both sides and cut first 3 sybols #
        else:
            print('Something went wrong')

    def setNewVersion(self):
        if self.getCurrentVersion() == self.newVersion:
            return False
        else:
            print(self.newVersion)
            # subprocess.run("sudo -S update-alternatives --set php /usr/bin/php" + self.newVersion, shell=True)

    def initPhpVersion(self):
        process = input("Your current php version: " + self.getCurrentVersion() + ". Continue? [y/n]: ").lower()
        if process in self.positiveRespone:
            self.setNewVersion()
        elif process in self.negativeRespone:
            return False
        else:
            self.initPhpVersion()


php = PHP()
newVersion = php.initPhpVersion()




