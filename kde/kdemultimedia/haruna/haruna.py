import info
from CraftConfig import *
from CraftOS.osutils import OsUtils

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.displayName = "Haruna"
        self.description = "Haruna video player"
        self.svnTargets["master"] = "https://invent.kde.org/multimedia/haruna.git"
                
        for ver in ["0.7.3"]:
            self.targets[ver] = f"https://invent.kde.org/multimedia/haruna/-/archive/v{ver}/haruna-v{ver}.tar.gz"
            self.targetInstSrc[ver] = f"haruna-v{ver}"
            self.archiveNames[ver] = f"haruna-v{ver}.tar.gz"
            
        self.targetDigests["0.7.3"] = (["8ef599a6b986fdff85067d9c9c47aa8d70f07e365446036247b8da1237d75bd4"], CraftHash.HashAlgorithm.SHA256)

        # patch needed for mpv master, mpv 0.34.0 doesn't have meson
        self.patchToApply["0.7.3"] = [("0001-remove-mpv_opengl_init_params_extra_exts-field.patch", 1)]
        self.patchToApply["master"] = [("0001-remove-mpv_opengl_init_params_extra_exts-field.patch", 1)]

        self.defaultTarget = "master"

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
        self.defines["executable"] = "bin\\haruna.exe"

        self.defines["icon"] = os.path.join(self.packageDir(), "haruna.ico")

        self.defines["mimetypes"] = ["video/mkv", "video/mp4", "video/ogm", "video/avi"]
        self.defines["file_types"] = [".mkv", ".mp4", ".ogm", ".avi"]

        self.ignoredPackages.append("binary/mysql")
        self.ignoredPackages.append("libs/dbus")

        return TypePackager.createPackage(self)

    def preArchive(self):
        # can't find library if it starts with lib
        if OsUtils.isWin() :
            utils.copyFile(os.path.join(self.archiveDir(), "bin", "org", "kde", "qqc2desktopstyle", "private", "libqqc2desktopstyleplugin.dll"),
                        os.path.join(self.archiveDir(), "bin", "org", "kde", "qqc2desktopstyle", "private", "qqc2desktopstyleplugin.dll"))
            utils.copyFile(os.path.join(self.archiveDir(), "bin", "org", "kde", "sonnet", "libsonnetquickplugin.dll"),
                        os.path.join(self.archiveDir(), "bin", "org", "kde", "sonnet", "sonnetquickplugin.dll"))

        return super().preArchive()
