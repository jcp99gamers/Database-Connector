import subprocess
import pkg_resources
import pathlib as pb
path = pb.Path(__file__).parent.resolve().as_posix() #Used for Python Files
file = path+"/requirements.txt"
# Read the requirements.txt file and extract the library names and versions
with open(file) as f:
    libs = [line.strip() for line in f]

# Check if each library exists and is up to date, and install/update it if necessary
for i, lib in enumerate(libs):
    try:
        pkg_resources.require(lib)
    except (ImportError, pkg_resources.VersionConflict):
        subprocess.check_call(['pip', 'install', '-U', lib])
        # Update the requirements.txt file with the latest version of the installed library
        dist = pkg_resources.get_distribution(lib)
        libs[i] = '{}=={}'.format(dist.project_name, dist.version)

# Write the updated requirements.txt file
with open(file, 'w') as f:
    f.write('\n'.join(libs))