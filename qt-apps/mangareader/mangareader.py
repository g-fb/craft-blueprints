import info
from CraftConfig import *
from CraftOS.osutils import OsUtils

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.svnTargets["master"] = "https://gitlab.com/g-fb/mangareader.git"
        
        for ver in ["1.6.0"]:
            self.targets[ver] = f"https://gitlab.com/g-fb/mangareader/-/archive/{ver}/mangareader-{ver}.tar.gz"
            self.targetInstSrc[ver] = f"mangareader-{ver}"
            self.archiveNames[ver] = f"mangareader-{ver}.tar.gz"
            
        self.targetDigests["1.6.0"] = (["3f1fd1af49d571029fe332daa8b14a3c7df2533adb8bb1bb52641ab20ae4849c"], CraftHash.HashAlgorithm.SHA256)
        self.defaultTarget = "1.6.0"
        self.displayName = "MangaReader"


    def setDependencies( self ):
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qarchive"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kconfigwidgets"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kio"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kxmlgui"] = None

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__(self):
        CMakePackageBase.__init__(self)

    def createPackage(self):
        self.defines["executable"] = "src\\mangareader.exe"
        self.defines["mimetypes"] = ["application/zip", "application/vnd.comicbook+zip", "application/x-7z-compressed", "application/x-cb7", "application/x-tar", "application/x-cbt", "application/vnd.rar", "application/vnd.comicbook-rar"]
        self.defines["file_types"] = [".zip", ".cbz", ".7z", ".cb7", ".tar", ".cbr", ".rar", ".cbr"]

        self.ignoredPackages.append("binary/mysql")
        self.ignoredPackages.append("libs/dbus")

        return TypePackager.createPackage(self)
 
