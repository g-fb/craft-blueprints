import info
from CraftConfig import *
from CraftOS.osutils import OsUtils

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.svnTargets["master"] = "https://invent.kde.org/multimedia/haruna.git"
                
        for ver in ["0.7.3"]:
            self.targets[ver] = f"https://invent.kde.org/multimedia/haruna/-/archive/v{ver}/haruna-v{ver}.tar.gz"
            self.targetInstSrc[ver] = f"haruna-v{ver}"
            self.archiveNames[ver] = f"haruna-v{ver}.tar.gz"
            
        self.targetDigests["0.7.3"] = (["8ef599a6b986fdff85067d9c9c47aa8d70f07e365446036247b8da1237d75bd4"], CraftHash.HashAlgorithm.SHA256)
        self.defaultTarget = "0.7.3"
        self.displayName = "Haruna"
        self.description = "Haruna video player"

    def setDependencies( self ):
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/ffmpeg"] = None
        self.runtimeDependencies["libs/dbus"] = None
        self.runtimeDependencies["libs/mpv"] = None
        self.runtimeDependencies["libs/qt5/qtgraphicaleffects"] = None
        self.runtimeDependencies["libs/qt5/qtquickcontrols2"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kirigami"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier2/kdoctools"] = None
        self.runtimeDependencies["kde/frameworks/tier2/kfilemetadata"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kio"] = None
        self.runtimeDependencies["kde/frameworks/tier3/qqc2-desktop-style"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kiconthemes"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kxmlgui"] = None

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__(self):
        CMakePackageBase.__init__(self)

    def createPackage(self):
        self.defines["executable"] = "src\\haruna.exe"

        self.defines["mimetypes"] = ["video/mkv", "video/mp4", "video/ogm", "video/avi"]
        self.defines["file_types"] = [".mkv", ".mp4", ".ogm", ".avi"]

        self.ignoredPackages.append("binary/mysql")
        self.ignoredPackages.append("libs/dbus")

        return TypePackager.createPackage(self)
