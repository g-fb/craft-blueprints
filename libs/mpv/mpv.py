import info
from CraftConfig import *
from Package.MesonPackageBase import *

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.displayName = "mpv"
        self.description = "Command line video player"
        self.svnTargets["master"] = "https://github.com/mpv-player/mpv.git"
        self.defaultTarget = "master"

    def setDependencies( self ):
        self.buildDependencies["python-modules/meson"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["binary/lua"] = None
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
        self.subinfo.options.configure.args = ["-Drubberband=disabled", "-Diconv=disabled", "-Dcplayer=false", "-Dlua=enabled", "-Dlibmpv=true"]
        self.subinfo.options.make.args = ["-C", self.buildDir()]

    def make(self):
        with utils.ScopedEnv(self._MesonBuildSystem__env()):
            return utils.system(Arguments(["meson", "compile", self.makeOptions(self.subinfo.options.make.args)]), cwd=self.workDir())
