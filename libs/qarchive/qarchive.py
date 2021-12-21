import info
from CraftConfig import *
from CraftOS.osutils import OsUtils

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.displayName = "QArchive"
        self.description = "QArchive is a cross-platform C++ library that modernizes libarchive. This library helps you to extract and compress archives supported by libarchive. The whole library itself is crafted to work perfectly well with the Qt event loop and thus its a perfect fit for your Qt projects."
        self.svnTargets["master"] = "https://github.com/antony-jr/QArchive.git"
        self.defaultTarget = "master"

    def setDependencies( self ):
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/libarchive"] = None

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        #self.subinfo.options.configure.args += ["-DBUILD_EXAMPLES=ON"]
