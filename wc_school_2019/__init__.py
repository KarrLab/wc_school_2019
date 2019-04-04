import pkg_resources

# read version
with open(pkg_resources.resource_filename('wc_school_2019', 'VERSION'), 'r') as file:
    __version__ = file.read().strip()