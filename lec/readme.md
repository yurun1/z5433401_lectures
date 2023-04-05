The `toolkit` shared folder 
============================================================================

This folder will include the codes discussed in class and in the lecture
notes. More files will be added later in the course

## Structure

```
<DROPBOX_SHARED_FOLDER>/
|
|__ data/                        <-- data files (discussed in the lectures)
|       ...
|__ lectures/                    <-- Scaffold version of the companion codes           
|   |__ solutions/                  <-- Final version of the companion codes           
|       ...
|__ webinars/                    <-- Codes discussed during class 
|       ...
|
|__ tk_utils.py                 <- OPTIONAL utilities module (see below)
```

The `lectures` folder
============================================================================

The `lectures` folder includes the "companion codes" discussed in the lectures. 

```
<DROPBOX_SHARED_FOLDER>/
|       ...
|__ lectures/                    <-- Scaffold version of the companion codes           
|   |__ solutions/                    <-- Will be populated after each lecture
|   |
|   |__ lec_avgs_example.py
|   |__ lec_fileio.py
|   |__ lec_pd_bools.py
|   |__ lec_pd_csv.py
|   |__ lec_pd_dataframes.py
|   |__ lec_pd_datetime.py
|   |__ lec_pd_groupby.py
|   |__ lec_pd_indexing.py
|   |__ lec_pd_joins.py
|   |__ lec_pd_numpy.py
|   |__ lec_pd_series.py
...
```

Below is the lecture in which each companion code is first discussed:


- Lecture 4.6:
  -  `lec_fileio.py`

- Lecture 5.1:
  -  `lec_avgs_example.py`

- Lecture 5.2:
  -  `lec_pd_series.py`
  -  `lec_pd_dataframes.py`

- Lecture 5.3:
  -  `lec_pd_numpy.py`

- Lecture 6.1:
  -  `lec_pd_indexing.py`

- Lecture 6.2:
  -  `lec_pd_csv.py`

- Lecture 7.1:
  -  `lec_pd_datetime.py`

- Lecture 9.1:
  -  `lec_pd_joins.py`

- Lecture 9.2:
  -  `lec_pd_bools.py`

- Lecture 9.3:
  -  `lec_pd_groupby.py`

The `tk_utils.py` module
============================================================================

This module is **optional**. It includes utilities to:

1. Download files from Dropbox
1. Backup files under the `toolkit` folder (in PyCharm)

## Usage:

1. Download the file `tk_utils.py` file and make sure it is saved under the
   `toolkit` folder:

   ~~~
   toolkit/
   | ... 
   |__ tk_utils.py             <- Put the `tk_utils.py` file here
   |__ toolkit_config.py       <- (you already have this file)
   ~~~

1. Make sure your `toolkit_config.py` file includes the variable `PRJDIR`
   (if you followed the instructions in Lecture 4.4, it will).  

1. Open the PyCharm console and type:

   ~~~
   >> import tk_utils
   >> help(tk_utils)
   ~~~

1. You should only use the functions `tk_utils.sync_dbox` and
   `tk_utils.backup`. 

  1. To backup the `toolkit` folder:

      ~~~ 
      >> import tk_utils
      >> tk_utils.backup()
      ~~~

  1. To download the files in the Dropbox shared folder:

      ~~~ 
      >> import tk_utils
      >> tk_utils.sync_dbox()
      ~~~


    
