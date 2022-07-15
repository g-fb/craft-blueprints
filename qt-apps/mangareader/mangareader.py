import info
from CraftConfig import *
from CraftOS.osutils import OsUtils

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.displayName = "MangaReader"
        self.description = "A manga reader for local files. Works with folders and archives (zip, rar, tar, 7z, cbz, cbr, cbt, cb7)."
        self.svnTargets["master"] = "https://github.com/g-fb/mangareader"
        self.defaultTarget = "2.0.4"
        
        for ver in ["2.0.4", "1.7.2"]:
            self.targets[ver] = f"https://github.com/g-fb/mangareader/archive/refs/tags/{ver}.tar.gz"
            self.targetInstSrc[ver] = f"mangareader-{ver}"
            self.archiveNames[ver] = f"mangareader-{ver}.tar.gz"

        self.targetDigests["2.0.4"] = (["da9d0323f5862b232a844fc7a46cf2fb84149075172c4da6d10c64ff2711cd28"], CraftHash.HashAlgorithm.SHA256)
        self.targetDigests["1.7.2"] = (["ac9e6ae8328874763d7a13f91dc71f459e63e80668badea85f1f79d614e11ba0"], CraftHash.HashAlgorithm.SHA256)


    def setDependencies( self ):
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["kde/plasma/breeze"] = None
        self.runtimeDependencies["kde/frameworks/tier1/karchive"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kconfigwidgets"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kio"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kxmlgui"] = None

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def createPackage(self):
        self.defines["executable"] = "bin\\mangareader.exe"

        # mangareader icons
        self.defines["icon"] = os.path.join(self.packageDir(), "mangareader.ico")
        self.defines["icon_png"] = os.path.join(self.sourceDir(), "mangareader", "icons", "windows", "150-apps-mangareader.png")
        self.defines["icon_png_44"] = os.path.join(self.sourceDir(), "mangareader", "icons", "windows", "44-apps-mangareader.png")


        self.defines["mimetypes"] = ["application/zip", "application/vnd.comicbook+zip", "application/x-7z-compressed", "application/x-cb7", "application/x-tar", "application/x-cbt", "application/vnd.rar", "application/vnd.comicbook-rar"]
        self.defines["file_types"] = [".zip", ".cbz", ".7z", ".cb7", ".tar", ".cbt", ".rar", ".cbr"]

        self.ignoredPackages.append("binary/mysql")
        self.ignoredPackages.append("libs/dbus")

        return TypePackager.createPackage(self)
 
