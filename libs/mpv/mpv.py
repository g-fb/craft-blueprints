import info
from CraftConfig import *
from CraftOS.osutils import OsUtils
from Package.MesonPackageBase import *

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.svnTargets["master"] = "https://github.com/mpv-player/mpv.git"
        
        #for ver in ["0.34.0"]:
            #self.targets[ver] = f"https://github.com/mpv-player/mpv/archive/refs/tags/v{ver}.tar.gz"
            #self.targetInstSrc[ver] = f"mpv-{ver}"
            #self.archiveNames[ver] = f"mpv-{ver}.tar.gz"

        #self.targetDigests["0.34.0"] = (["f654fb6275e5178f57e055d20918d7d34e19949bc98ebbf4a7371902e88ce309"], CraftHash.HashAlgorithm.SHA256)
        #self.defaultTarget = "0.34.0"
        self.defaultTarget = "master"
        self.displayName = "mpv"
        self.description = "Command line video player"

    def setDependencies( self ):
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/ffmpeg"] = None
        self.runtimeDependencies["libs/libass"] = None
        self.runtimeDependencies["libs/uuid"] = None
        self.runtimeDependencies["libs/libva"] = None
        self.runtimeDependencies["libs/libvdpau"] = None
        self.runtimeDependencies["libs/zlib"] = None
        self.runtimeDependencies["libs/libarchive"] = None
        self.runtimeDependencies["libs/lcms2"] = None
        self.runtimeDependencies["libs/jack2"] = None
        self.runtimeDependencies["libs/libjpeg-turbo"] = None
        self.runtimeDependencies["libs/rubberband"] = None

class Package(MesonPackageBase):
    def __init__(self, **args):
        MesonPackageBase.__init__(self)
        self.subinfo.options.configure.args += ["-Dlibmpv=true", "-Dcplayer=false", "-Djpeg=disabled"]
