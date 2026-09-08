from os.path import join

from . import fabric, quilt

BASE_DIR = "ornithe"

JARS_DIR = join(BASE_DIR, "jars")
LIBRARIES_DIR = join(BASE_DIR, "libraries")
META_DIR = join(BASE_DIR, "meta-v3")

META_URL = "https://meta.ornithemc.net/v3/versions"
MAVEN_URL = "https://maven.ornithemc.net/releases"

INTERMEDIARY_GENERATION = 2

INTERMEDIARY_COMPONENT = "net.ornithemc.calamus-intermediary"

JAVA_MAJOR = 25
JAVA_NAME = "java-runtime-epsilon"

LOADERS = {
    "fabric": {
        "uid": "net.ornithemc.fabric-loader",
        "name": "Ornithe Fabric Loader",
        "prefix": "fabric",
        "maven": "https://maven.fabricmc.net",
        "jars_dir": fabric.JARS_DIR,
        "installer_info_dir": fabric.INSTALLER_INFO_DIR,
    },
    "quilt": {
        "uid": "net.ornithemc.quilt-loader",
        "name": "Ornithe Quilt Loader",
        "prefix": "loader",
        "maven": "https://maven.quiltmc.org/repository/release",
        "jars_dir": quilt.JARS_DIR,
        "installer_info_dir": quilt.INSTALLER_INFO_DIR,
    },
}
