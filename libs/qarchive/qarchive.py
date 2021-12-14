import info
from CraftConfig import *
from CraftOS.osutils import OsUtils

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.svnTargets["master"] = "https://github.com/antony-jr/QArchive.git"
        
        for ver in ["2.1.1"]:
            self.targets[ver] = f"https://github.com/antony-jr/QArchive/archive/refs/tags/v{ver}.tar.gz"
            self.targetInstSrc[ver] = f"QArchive-{ver}"
            self.archiveNames[ver] = f"QArchive-{ver}.tar.gz"
        
        self.targetDigests['2.1.1'] = (['4ed51121a5bc9b5981d2fa3927f951a6a91ccca233d6b6dc4fef55b4ca5a2d92'], CraftHash.HashAlgorithm.SHA256)
        self.defaultTarget = "2.1.1"
        self.displayName = "QArchive"


    def setDependencies( self ):
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/libarchive"] = None

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        # use openssl for encryption
        self.subinfo.options.configure.args += "-DQARCHIVE_STATIC=OFF"
        
