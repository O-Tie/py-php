import os
import sys
import subprocess
import getpass


class PHP(object):

    positive_response = ["yes", "y", "ok", "да", "д"]
    negative_response = ["no", "n", "nok", "нет", "н"]
    php_versions = ["5.6", "7.0", "7.1", "7.2", "7.3"]
    _current_version = None
    _new_version = None
    _sudo_pass = None

    def get_new_version(self):
        return self._new_version

    def set_new_version(self, version):
        if version is not None:
            self._new_version = version

    def set_current_version(self, version):
        if version is not None:
            self._current_version = version

    def get_sudo_pass(self):
        return self._sudo_pass

    def set_sudo_pass(self, s_pass):
        if s_pass is not None:
            self._sudo_pass = s_pass

    def get_pass(self):
        passw = getpass.getpass("Sudo pass: ")
        self.set_sudo_pass(passw)

    def get_wanted_version(self):
        wanted_version = input("Write php version: ")
        if wanted_version in self.php_versions:
            self.set_new_version(wanted_version)
            return wanted_version
        else:
            print("Check available version please")
            self.get_wanted_version()

    def get_current_version(self):
        php_c = subprocess.run('echo ' + self._sudo_pass + ' | sudo -S php -v', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
        php_c_list = php_c.split()

        if php_c_list[0].strip() == "PHP":
            current_version = php_c_list[1].strip()[:3]  # Cut whitespaces from both sides and cut first 3 symbols #
            self.set_current_version(current_version)
            return current_version
        else:
            sys.stdout.write("\033[1;31m")
            print('Something went wrong')
            return False

    def set_wanted_version(self):
        if self.get_current_version() == self._new_version:
            return False
        else:
            subprocess.run("echo " + self._sudo_pass + " | sudo -S update-alternatives --set php /usr/bin/php" + self._new_version + ";"
                           + "sudo -S a2dismod php" + self._current_version + ";"
                           + "sudo -S a2enmod php" + self._new_version + ";"
                           + "sudo -S service apache2 restart;", shell=True)
            sys.stdout.write("\033[0;32m")
            print("PHP " + self._new_version + " already enabled")


    def init_php_version(self):
        self.get_pass()
        process = input("Your current php version: " + self.get_current_version() + ". Continue? [y/n]: ").lower()
        if process in self.positive_response:
            self.get_wanted_version()
            self.set_wanted_version()
        elif process in self.negative_response:
            return False
        else:
            self.init_php_version()


php = PHP()
newVersion = php.init_php_version()
