""" tk_utils.py

The `toolkit` utilities module. 

IMPORTANT: This module should be placed directly under your toolkit project
folder:

    toolkit/   
    | ...
    |__ tk_utils.py         <- This file
    |__ toolkit_config.py   <- Your config file (REQUIRED)

IMPORTANT: This module is OPTIONAL and should not be modified. Also, it
includes Python concepts/libraries we did not (and will not) discuss in this
course (e.g., the modules "requests" and "zipfile"). Please use this module
"as is" and do not worry about the implementation.

IMPORTANT: This module requires that the `toolkit_config.py` module includes
the PRJDIR variable (which must be set to your PyCharm project folder).

If you followed the instructions in Lecture 4.4, you are all set!

    toolkit/    <- PyCharm project folder (PRJDIR in toolkit_config.py)
    | ...
    |__ toolkit_config.py   <- REQUIRED



Usage
-----

To synchronize the Dropbox files, open the PyCharm console and type:

    >> import tk_utils
    >> tk_utils.sync_dbox()

This will download the current version of the Dropbox shared folder and place
the files under 'toolkit/_dropbox'. All existing files will be replaced:

 <DROPBOX>/
 |__ toolkit/            <- Dropbox shared folder (SOURCE)
 |   |__ data/           
 |   |__ lectures/       
 |   |    ...
 
 toolkit/               <- PyCharm project folder 
 |
 |__ _dropbox/           <- DESTINATION (only files under this folder will be updated)
 |   |__ data/               <- Same as <DROPBOX>/toolkit/data above
 |   |__ lectures/           <- Same as <DROPBOX>/toolkit/lectures above
 |   |   ...                 <- Same as <DROPBOX>/toolkit/... above
 | ...
 |__ data/               <- NOT a destination (will not be updated)
 |__ lectures/           <- NOT a destination (will not be updated)
 |   ...                 <- NOT a destination (will not be updated)

If the _dropbox folder does not exist, it will be created


To backup the contents of your toolkit project folder, open the PyCharm
console and type:

    >> import tk_utils
    >> tk_utils.backup()

This will backup the files to a "dated" folder inside "_backup". Note that
the backup files will EXCLUDE system files/folders, the "_dropbox" folder
described above, and the "_backup" folder itself.

For example, suppose you only have the following files under toolkit:


 toolkit/               <- PyCharm project folder 
 |
 |__ toolkit_config.py
 |__ tk_utils.py        <- this module

After the backup, your toolkit folder will look like this:

 toolkit/               <- PyCharm project folder 
 |
 |__ _backup/                       <- Will be created 
 |  |__ <YYYY-MM-DD-HH:MM:SS>/          <- Represents the time of the backup
 |  |  |__ toolkit_config.py                <- backup
 |  |  |__ tk_utils.py                      <- backup
 |
 |__ toolkit_config.py              <- original (not modified)
 |__ tk_utils.py                    <- original (not modified)

"""

# IMPORTANT: DO NOT MODIFY THIS MODULE IN ANY WAY

import pathlib
import shutil
import zipfile
import requests
import datetime as dt

import toolkit_config as cfg


DROPBOX_URL = 'https://www.dropbox.com/sh/ru1p00ayfbjhvlr/AABkwVoapTk-YaV0qdc622l6a?dl=1'
PRJDIR = pathlib.Path(cfg.PRJDIR)

BACKUP_DIR = '_backup'
DBOX_DIR = '_dropbox'
DIRS_TO_EXCL = [
        'venv',
        '.idea',
        BACKUP_DIR,
        DBOX_DIR,
        '__pycache__',
        ]

class _Msg(list):
    """ Message to be printed
    """

    def add(self, line : str,
            sep : bool = False,
            strip : bool = False,
            newline : bool = False,
            bold : bool = False,
            ):
        """  Adds a line line to the message

        Parameters
        ----------
        line : str
            The line to add
        sep : bool
            If True, insert separators
            Defaults to False
        strip : bool
            If True, strip the line first
            Defaults to False
        newline : bool
            If True, add a newline char after the (stripped) line
            Defaults to False
        bold : bool
            If True, line (and separators) will be printed in bold
            Defaults to False

        """
        new = [line if strip is False else line.strip()]
        if sep is True:
            _sep = '-' * max(len(line), 40)
            new = [_sep] + new + [_sep]
        if newline is True:
            new.append('')
        if bold is True:
            #   [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code)
            new = [f"\033[1m{x}\033[0m" for x in new]

        self.extend(new)

    def print(self):
        """ Prints the current message (list of strings)
        """
        print('\n'.join(self))





def sync_dbox():
    """ Downloads the files from the Dropbox shared folder into "_dropbox".

    This function will download all files from the shared folder under
    DROPBOX_URL into the following folder:

    toolkit/
    |__ _dropbox/       <- Destination

    Files under "_dropbox" will be replaced.

    Usage
    -----

    >> import tk_utils
    >> tk_utils.sync_dbox()

    """
    msg = _Msg()
    msg.add("Downloading Dropbox files...", sep=True, bold=True)
    msg.print()

    tmp = PRJDIR.joinpath('toolkit_dropbox.zip')
    dst = PRJDIR.joinpath(DBOX_DIR)

    if not dst.exists():
        dst.mkdir(parents=True)

    r = requests.get(DROPBOX_URL)
    with open(tmp, 'wb') as fobj:
        fobj.write(r.content)

    with zipfile.ZipFile(tmp) as zf:
        zf.extractall(dst)

    tmp.unlink()
    print('Done!')


def backup(show_folder : bool = False):
    """ Backup files under the toolkit project folder

    This function will copy all (non-system) files under "toolkit" to a dated folder
    inside "toolkit/_backup". A new dated folder will be created every time
    this function is called.

    This function will exclude system files, hidden files (e.g., files
    starting with '.'),  the Dropbox folder, and the backup folder itself.

    Parameters
    ----------
    show_folder : bool
        If True, prints the location of the destination folder.
        Ignored if the "_backup" folder does not exist (will always be printed)
        Defaults to False

    Usage
    -----
    >> import tk_utils
    >> tk_utils.backup()


    Example
    -------
    Suppose you only have the following files under toolkit:

     toolkit/               <- PyCharm project folder 
     |
     |__ toolkit_config.py
     |__ tk_utils.py        <- this module

    After the backup, your toolkit folder will look like this:

     toolkit/               <- PyCharm project folder 
     |
     |__ _backup/                       <- Will be created 
     |  |__ <YYYY-MM-DD-HH:MM:SS>/          <- Represents the time of the backup
     |  |  |__ toolkit_config.py                <- backup
     |  |  |__ tk_utils.py                      <- backup
     |
     |__ toolkit_config.py              <- original (not modified)
     |__ tk_utils.py                    <- original (not modified)


    """
    now = dt.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    bkroot = PRJDIR.joinpath(BACKUP_DIR)

    if not bkroot.exists():
        show_folder = True


    msg = _Msg()
    msg.add("Backing up toolkit folder...", sep=True, bold=True)
    if show_folder is True:
        msg.add(f'''Destination:
            
    toolkit/
    |__ {BACKUP_DIR}/
    |   |__ {now}/      <- New folder''', strip=True, newline=True)
    msg.print()


    def _copy(src, dst):
        """ Simplified version of my brutils.copy_tree function
        """
        if src.name.startswith('.'):
            return
        elif src.is_dir() and src.name not in DIRS_TO_EXCL:
            children = sorted(src.iterdir())
            # Copy empty directory and filter non-empty ones
            if len(children) == 0:
                shutil.copytree(src, dst)
            else:
                [_copy(p, dst.joinpath(p.name)) for p in children]
        elif src.is_file():
            if not dst.parent.exists():
                dst.parent.mkdir(parents=True)
            shutil.copy2(src, dst)
        else:
            # This should only happen if file is a symbolic link
            return

    bkdir = bkroot.joinpath(now)
    if not bkdir.exists():
        bkdir.mkdir(parents=True)

    for src in PRJDIR.iterdir():
        _copy(src, bkdir.joinpath(src.name))

    print('Done!')



if __name__ == "__main__":
    pass
    backup(show_folder=True)
    #sync_dbox()




