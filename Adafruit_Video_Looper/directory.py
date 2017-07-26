# Copyright 2015 Adafruit Industries.
# Author: Tony DiCola
# License: GNU GPLv2, see LICENSE.txt
from datetime import datetime, time
class DirectoryReader(object):

    def __init__(self, config):
        """Create an instance of a file reader that just reads a single
        directory on disk.
        """
        self._load_config(config)

    def _load_config(self, config):
        self._path1 = config.get('directory', 'path1')
        self._path2 = config.get('directory', 'path2')
        self._path3 = config.get('directory', 'path3')

    def search_paths(self):
        """Return a list of paths to search for files."""

        #aqui debe ir el control de los horarios
        now = datetime.now()
        now_time = now.time()


            #matutino
            if now_time >= time(05,00) and now_time <= time(11,00):
                return [self._path1]

            #vespertino
            elif now_time >= time(11,00) and now_time <= time(20,00):
                return [self._path2]

            #diurno
            elif now_time >= time(20,00) and now_time <= time(04,59):
                return [self._path3]
    

    def is_changed(self):
        """Return true if the file search paths have changed."""
        # For now just return false and assume the path never changes.  In the
        # future it might be interesting to watch for file changes and return
        # true if new files are added/removed from the directory.  This is 
        # called in a tight loop of the main program so it needs to be fast and
        # not resource intensive.
        return False

    def idle_message(self):
        """Return a message to display when idle and no files are found."""
        return 'No files found in {0}'.format(self._path)


def create_file_reader(config):
    """Create new file reader based on reading a directory on disk."""
    return DirectoryReader(config)
