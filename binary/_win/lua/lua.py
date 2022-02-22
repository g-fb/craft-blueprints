import shutil

import info
from Package.BinaryPackageBase import *

class subinfo(info.infoclass):
    def setTargets(self):
        for version in ['5.2.4']:
            self.targets[version] = 'https://gitlab.com/g-fb/mpv-binaries/-/raw/main/lua-5.2.4_Win64_dllw6_lib.zip'
        self.defaultTarget = '5.2.4'

    def setDependencies(self):
        self.buildDependencies["virtual/bin-base"] = None

class Package(BinaryPackageBase):
    def __init__(self):
        BinaryPackageBase.__init__(self)

    def install(self):
        utils.copyFile(os.path.join(self.workDir(), "liblua52.a"),
                       os.path.join(self.installDir(), "bin", "liblua52.a"))
        utils.copyFile(os.path.join(self.workDir(), "lua52.dll"),
                       os.path.join(self.installDir(), "bin", "lua52.dll"))
        utils.copyDir(os.path.join(self.workDir(), "include"),
                      os.path.join(self.installDir(), "include"))

        return True
