import info
from CraftConfig import *
from CraftOS.osutils import OsUtils

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.displayName = "MangaReader"
        self.description = "A manga reader for local files. Works with folders and archives (zip, rar, tar, 7z, cbz, cbr, cbt, cb7)."
        self.defaultTarget = "master"
        self.svnTargets["master"] = "https://github.com/g-fb/mangareader"

    def setDependencies( self ):
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qarchive"] = None
        self.runtimeDependencies["kde/plasma/breeze"] = None
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
        # used by QArchive
        self.subinfo.options.configure.args += ["-DQT_VERSION_MAJOR=5"]

    def createPackage(self):
        self.defines["executable"] = "bin\\mangareader.exe"

        # mangareader icons
        self.defines["icon"] = os.path.join(self.packageDir(), "mangareader.ico")
        self.defines["icon_png"] = os.path.join(self.sourceDir(), "mangareader", "icons", "windows", "150-apps-mangareader.png")
        self.defines["icon_png_44"] = os.path.join(self.sourceDir(), "mangareader", "icons", "windows", "44-apps-mangareader.png")


        self.defines["mimetypes"] = ["application/zip", "application/vnd.comicbook+zip", "application/x-7z-compressed", "application/x-cb7", "application/x-tar", "application/x-cbt", "application/vnd.rar", "application/vnd.comicbook-rar"]
        self.defines["file_types"] = [".zip", ".cbz", ".7z", ".cb7", ".tar", ".cbr", ".rar", ".cbr"]

        self.ignoredPackages.append("binary/mysql")
        self.ignoredPackages.append("libs/dbus")

        return TypePackager.createPackage(self)
