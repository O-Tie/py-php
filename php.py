import os
import subprocess

class PHP(object):

    positiveRespone = ["yes", "y", "ok"]
    negativeRespone = ["no", "n", "nok"]
    cmdCurrent = ["sudo", "-S", "php", "-v"]
    phpVersions = ["5.6", "7.0", "7.1", "7.2", "7.3"]

    def getNewVersion(self):
        wantedVersion = str(input("Write php version: "))
        if wantedVersion in self.phpVersions:
            return wantedVersion
        else:
            print("Check avaliavle version please")
            self.getNewVersion()

    def getCurrentVersion(self):
        phpC = subprocess.run(self.cmdCurrent, stdout=subprocess.PIPE).stdout.decode('utf-8')

        phpCList = phpC.split()

        if phpCList[0].strip() == "PHP":
            return phpCList[1].strip()[:3]  # Cut whitespaces from both sides and cut first 3 sybols #
        else:
            print('Something went wrong')

    def setNewVersion(self):
        print('new version change')

    def initPhpVersion(self):
        process = input("Your current php version: " + self.getCurrentVersion() + ". Continue? [y/n]: ")
        if self.getProcess(process):
            self.setNewVersion()
        else:
            return False


    def getProcess(self, response):
        if response in self.positiveRespone:
            return True
        elif response in self.negativeRespone:
            return False
        else:
            self.initPhpVersion()

php = PHP()
newVersion = php.initPhpVersion()




