# -*- coding: utf-8 -*-
# Copyright (C) 2021  R.Cheshami
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU2 General Public License 2 as published by
# the Free Software Foundation
# An Audio MetaData Manager Application.
# Author : R.Cheshami
# Company : Adak Free Way .. http://afw.ir

import sys, os
import glob2
import meyed3
import logging
import enum
from pathlib import Path

class SIZE_UNIT(enum.Enum):
    BYTES = 1
    KiB = 2
    MiB = 3
    GiB = 4
    TiB = 5

class MD3(object):
    """docstring for MD3"""
    def __init__(self, start_time, *args):
        super(MD3, self).__init__()

        clear = lambda: os.system('clear')
        clear()

        self.start_time = start_time
        print(u'Start Time:', self.start_time)

        self.path = ''.join((str(Path.home()), '/Music/md3/'))
        self.audio_file = 'donya.mp3'
                        
        self.csv_filename = 'md3.csv'
        self.mp3 = ''
        self.mp3SongsData = []
        self.oggs = ''
        self.oggSongsData = []

        self.pf = ''
        self.recursive = False

        self.myMP3s = meyed3

        self.wellcome()

    def logMessage(message,file,revision,printMessage=True):
        message_time=time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
        message=myself+" "+revision+" "+message_time+" "+message
        if printMessage:
            print(message)
        message+="\n"
        if file:
            file.write(message)
            file.flush()

    def get_logger(self, msg='',cfname=None, name=None, level=logging.DEBUG, create_file=False):
        import inspect
        log = logging.getLogger(__name__)
        # get_logger('msg', 'MD3Logger', 'WARNING')
        if name is None:
                name = inspect.stack()[1][1].split('.')[0]
        formatter = logging.Formatter(
                "MD3 %(levelname)s Logging Message: %(asctime)s - %(process)d -  - %(threadName)s - %(name)s %(message)s")

        log = logging.StreamHandler()
        log.setLevel(level)
        log.setFormatter(formatter)
        if create_file:
                # create file handler for logger.
                fh = logging.FileHandler('md3.log')
                fh.setLevel(level)
                fh.setFormatter(formatter)
                logging.root.addHandler(fh)
        logging.root.addHandler(log)
        return log

    def getch(self):
        """Gets a single character from standard input.
        Does not echo to the screen."""
        import termios
        import tty

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
        return _getch()

    def get_args(self):
        import argparse

        description = (
                        "Get and Set your Music MetaData in [CSV file].\n"
                        "You set a path with an argumant -p, then application\n"
                        "create a CSV file, with all MetaData Tags of all your Musics\n"
                        "you set for application [recursivly]."
        )
        parser = argparse.ArgumentParser(prog='md3.sh', description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('--path', '-p', required=False, help="if path+file writed: Display Metadata[s] of this file[s]\
                            if just a path inserted Music path or directory. Default is user's Home Music Directory")
        parser.add_argument('--csvin', '-i', required=False, help="The Musics Metadata's CSV file to Update Musics Metadatas")
        parser.add_argument('--csvout', '-o', required=False, help="Name of Music Metadata CSV file.Default is md3.csv")
        parser.add_argument('--mfile', '-m', required=False, help="")
        parser.add_argument('--recursive', '-r', required=False, help="Recursive")

        return parser.parse_args()

    def colored(self, text, color=None):
        '''Returns colored text'''

        if color:
            if color == 'red':
                text = '\033[91m{}\033[00m'.format(text)
            elif color == 'green':
                text = '\033[92m{}\033[00m'.format(text)
            elif color == 'yellow':
                text = '\033[93m{}\033[00m'.format(text)
            elif color == 'blue':
                text = '\033[94m{}\033[00m'.format(text)
            elif color == 'perpel':
                text = '\033[95m{}\033[00m'.format(text)
            elif color == 'lightblue':
                text = '\033[96m{}\033[00m'.format(text)
            elif color == 'c1':
                text = '\033[90m{}\033[90m'.format(text)
            elif color == 'c2':
                text = '\033[88m{}\033[00m'.format(text)
            elif color == 'c3':
                text = '\033[89m{}\033[00m'.format(text)
            elif color == 'darkblue':
                text = '\033[90m{}\033[00m'.format(text)
            else:
                return text
        else:
            return text
        return text

    def wellcome(self):
        print(u'{0}{1}{2}{3}{4}{1}{0}'.format(
        '\n', '-'*30, '[', self.colored('MD3', color='red'), ']'))
        print(u'\n\t\u2554', end='')
        for i in range(25):
            print(u'\u2550', end='')
        print(u'\u2557\n\t\u2551', u' ## WellCome To MD3 ## ', u'\u2551\n\t\u255a', end='')
        for i in range(25):
            print(u'\u2550', end='')
        print(u'\u255d\n')
        self.main()

    def get_mp3s_files(self):
        if self.recursive == False:
            self.mp3s = glob2.glob(self.path + '*.mp3')
        else:
            self.mp3s = glob2.glob(self.path + '**/*.mp3')
        return self.mp3s

    def get_oggs_files(self):
        try:
            if os.path.exists(self.path):
                if self.answer == '2':
                    self.oggs = glob2.glob(self.path + '*.ogg')
                elif self.answer == '3':
                    self.oggs = glob2.glob(self.path + '**/*.ogg')
        except Exception:
            print(u'{} Not find.'.format(self.pf))
        return self.oggs

    def is_answer_corect(self):
        try:
            self.answer = int(raw_input('Enter a value (0..12). '))
        except ValueError:
            print('Invalid input. Enter a value from 0 till 12.')

        if not self.answer in range(0, 12):
            print('Invalid input. Enter a value between 0 - 12.')

        return self.answer

    def check_path(self):
        while True:
            try:
                if not(os.path.exists(self.path)):
                    print("Enter Valid Path or Filename : ", end="\n\t")
                    self.path = input('')
                    if self.path[-1] != '/':
                        self.path += '/'
            except IOError:
                print('Invalid path or Filename...', end="\r")
            break;
        return(self.path)

    def check_file(self):
        while True:
            try:
                if not(os.path.isfile(self.audio_file)):
                    print(u'The {} file is not there.'.format(self.audio_file))
                    self.audio_file = input('Enter Full Path of  File location? ')
                if self.audio_file == '':
                    self.main()
                else:
                    break;
            except IOError:
                print('There is Not this filename..')
            except TypeError:
                print('Invalid Filename...')
        return(self.audio_file)

    """
    def menu(self):
        menu = {"1":(" - Get Tags of a Music",my_add_fn),
                "2":(" - Get Tags of a path Musics",my_quit_fn)
               }
        for key in sorted(menu.keys()):
             print(key+":" + menu[key][0])

        ans = raw_input("Make A Choice")
        menu.get(ans,[None,invalid])[1]()
    """
    def edit_tag():
        ## [\[{(:" .]*[W]{0,3}[.]{0,2}[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}[-_@\[ )\]]{0,4}$
        ## @[a-zA-Z0-9 ]*
        ## [ ]$
        ## [ا-ی]*
        pass

    def rename(self):
        if self.SongData[2] != '':
            from pathlib import Path
            f = Path(self.SongData[17]+self.SongData[0])
            print(u'File Renamed to : {}'.format(f.rename(Path(f.parent, "{}_{}{}".format(self.SongData[1], self.SongData[2], f.suffix)))))
        else:
            print(u'-- !!! This file dont have Title Tag...')

    def convert_unit(self, size_in_bytes, unit):
        """
        convert the size from bytes to other units linke KB, MB,...etc
        """
        if unit == SIZE_UNIT.KiB:
            return size_in_bytes/1024
        elif unit == SIZE_UNIT.MiB:
            return size_in_bytes/(1024*1024)
        elif unit == SIZE_UNIT.GiB:
            return size_in_bytes/(1024*1024*1024)
        elif unit == SIZE_UNIT.TiB:
            return size_in_bytes/(1024*1024*1024*1024)
        else:
            return(size_in_bytes)

    def splitCSVlist(self, csvlist):
        #get_logger('MD3Logger Start Split CSV file', 'MD3Logger', 'DEBUG')
        __mp3s = []
        for __row in self.csvlist:
            if __row[17] != 'Path':
                __fp = ''.join((__row[17], __row[0]))
                print('Read Tags Of {} File From CSV'.format(__fp))
                __mp3s.append(__fp)
        return __mp3s

    def correctPath(self, csvlist):
        #get_logger('MD3Logger Start fix path of CSV file', 'MD3Logger', 'DEBUG')
        for __row in self.csvlist:
            __row[16] = ''.join((__row[16], '/'))
            print('Path Was Fixed.')
        return self.csvlist

    def show_Tags_Column(self):
        for tag in self.SongsData:
        #get_logger('MD3Logger Start Showing all Tags of Eyed3 Song Object', 'MD3Logger', 'DEBUG')
            print(u'{:12} : {}'.format('File Name', tag[0]))
            print(u'{:12} : {}'.format('Artist(s)', tag[1]))
            print(u'{:12} : {}'.format('Title', tag[2]))
            print(u'{:12} : {}'.format('Album', tag[3]))
            print(u'{:12} : {}'.format('Album Artist', tag[4]))
            print(u'{:12} : {} {} : {}'.format('Track Number', tag[5], 'In', tag[6]))
            print(u'{:12} : {} {} : {}'.format('Disk Number', tag[7], ', All Disks:', tag[8]))
            print(u'{:12} : {}'.format('Date', tag[9]))
            print(u'{:12} : {}'.format('Gener', tag[10]))
            print(u'{:12} : {}'.format('Comments', tag[11]))
            print(u'{:12} : {}'.format('Publisher', tag[12]))
            print(u'{:12} : {}'.format('Lyrics', tag[13]))
            print(u'{:12} : {}'.format('ID3 Version', tag[14]))
            print(u'{:12} : {}'.format('Tag Size', tag[15]))
            print(u'{:12} : {} MiB'.format('File Size', self.convert_unit(float(tag[21]), SIZE_UNIT.MiB)))
            print(u'{:12} : {}'.format('Path', tag[17]))
            print(u'{:12} : {}'.format('Extention', tag[18]))
            print(u'{:12} : {}'.format('Created', tag[19]))
            print(u'{:12} : {}'.format('Modified', tag[20]))
            print(u'------------------------------------')
        return(True)

    def show_Tags_Row(self):
        #get_logger('MD3Logger Start Showing all Tags of Eyed3 Song Object', 'MD3Logger', 'DEBUG')
        for tag in self.SongsData:
            try:
                print(tag[0])
                print(u'{:35} | {:35} | {:30} | {:25} | {:15}'.format(
                    'Artist(s)', 'Title', 'Album', 'Album Artist', 'Date'))
                print(u'{:35} | {:35} | {:30} | {:25} | {:15}'.format(
                    tag[1], tag[2], tag[3], tag[4], tag[9]))
                print(u'------------------------------------')
            except UnicodeEncodeError as unerr:
                print(u'Unicode Error... Bad file name.{}'.format(unerr))
                return(False)
            except IndexError as inerr:
                print(u'{}'.format(inerr))
                return(False)
        return(True)

    def readCSVf(self, pf):
        import csv
        print(u'Opening {} CSV MetaData File ',self.pf)
        #get_logger('MD3Logger Start Read CSV file', 'MD3Logger', 'DEBUG')
        with open(self.pf) as __csvfile:
            print('{} File Was Opened'.format(self.pf))
            __csvlist = csv.reader(__csvfile)
            return list(__csvlist)

    def makeCSVf(self, pf):
        import csv
        print(u'Creating New Music MetaData File ',self.pf)
        try:
            with open(self.pf, 'w', newline='') as csvfile:
                fieldnames = ['File Name','Artist', 'Title', 'Album', 'Album Artists', 'Track Number',
                    'Totall Tracks', 'Disk Number', 'All Disks','Date', 'Gener', 'Comments',
                    'Publisher','Lyrics', 'ID3 Version', 'Tag Size', 'Size (MiB)', 'Path',
                    'Extention', 'Last Access',
                    'Last Modify', 'CoverArt']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
            csvfile.close()
        except IOError:
            print(u'Error: File {} Was Not Created.'.format(self.pf))
        else:
            print(u'File {} was created. and Header of CSV was added.'.format(self.pf))
        return

    def saveCSVf(self):
        import csv, os
        #get_logger('MD3Logger Start Save Tags in CSV file', 'MD3Logger', 'DEBUG')
        try:
            if not os.path.exists(self.pf):
                self.makeCSVf(self.pf)
            with open(self.pf, 'a', newline='') as __csvfile:
                for __row in self.SongsData:
                    writer = csv.DictWriter(__csvfile, __row)
                    writer.writeheader()
                print(u'The Tags Was writed to CSV file.')
            __csvfile.close()
        except IOError:
            print(u'\t-- File was not find!!!')
        else:
            print(u' -- CSV file Saved.')
        return True

    def saveJSONf(self):
        import json
        print(u'Creating New Music MetaData File ',self.pf)
        try:
            with open(self.pf, 'w', newline='') as __jsonfile:
                for tag in list(self.SongsData):
                    print(tag[0])
                    if tag[0] != None:
                        fieldnames = {'File': tag[0],
                                      'Tags': [
                                          {'Artist': tag[1],
                                           'Title': tag[2],
                                           'Album': tag[3],
                                           'Album Artists': tag[4],
                                           'Track Number': tag[5],
                                           'In': tag[6],
                                           'Disk Number': tag[7],
                                           'All Disks': tag[8],
                                           'Date': tag[9],
                                           'Gener': tag[10],
                                           'Comments': tag[11],
                                           'Publisher': tag[12],
                                           'Lyrics': tag[13],
                                           'ID3 Version': tag[14],
                                           'Tag Size': tag[15],
                                           'File Size': float(tag[21]),
                                           'Path': tag[17],
                                           'Extention': tag[18],
                                           'Created': tag[19],
                                           'Modified': tag[20]}
                                          ]
                                      }
                    json.dump(fieldnames, __jsonfile, ensure_ascii=False, sort_keys=False, indent=4)
                    print(u'tag Writed To the file.')
            __jsonfile.close()
        except IOError:
            print(u'Error: File {} Was Not Created.'.format(self.pf))
        else:
            print(u'File {} was created. and Header of CSV was added.'.format(self.pf))
        return True

    def rename(self, audiofile):
        new_filename = "sample/tagged/{0}-{1}.mp3".format(audiofile.tag.artist,
                    audiofile.tag.title)
        os.rename('samples/tagged/song1.mp3', new_filename)

    def quit(self):
        import datetime
        print(u'\nBye.\n\nEnd Time: {}'.format(datetime.datetime.now()))
        print(u'Tottal Time in This Program: {}'.format(datetime.datetime.now()-self.start_time))
        exit(0)

    def main(self, *args):
        print("Your Default(Entered) path is {} ? ".format(self.path))
        self.answer = self.getch()
        if self.answer == 'n':
            self.path = ''
            self.check_path()
        print("""What Do You Want To Do ? (Enter the number)\n
            \t1 - Get Tags of the Music\n
            \t2 - Get Tags of the path Musics\n
            \t3 - Get Tags of the path Musics Recursive\n
            \t4 - Create CSV file for Music(s) Metadata of this path.\n
            \t5 - Create CSV file for this path Recursive.\n
            \t6 - Create JSON file for Musics Metadata of this path.\n
            \t7 - Create JSON file for this path Recursive.\n
            \t8 - Save Musics Tag from a CSV file\n
            \t9 - Save Musics Tag from a JSON file\n
            \t10 - Rename file to Artist_Title.mp3\n
            \t11 - Rename files in this path to Artist_Title.mp3\n
            \t12 - Rename files in this path to Artist_Title.mp3 Recursive\n
            \tC - Clear Screen\n
            \t0 - Quite""")

        self.answer = input()

        if self.answer == '1':
            MD3.get_logger('Get a mp3 file MetaData.', name=__name__)
            print("Tags of {} file? (y/n) : ".format(self.audio_file))
            self.answer = self.getch()
            if self.answer == 'n':
                self.audio_file = ''
                self.audio_file = input("Enter Your Music File Name : ")
            self.check_file()
            os.path.exists(self.audio_file)
            self.mp3SongData = meyed3.get_Tags(self.audio_file)
            self.show_Tags_Column(self.mp3SongData)
            self.main()

        elif self.answer == '2' or self.answer == '3':
            self.SongsData = ''
            MD3.get_logger('Get mp3 file MetaData.', name=__name__)
            if self.answer == '3':
                MD3.get_logger('Get mp3 file(s) MetaData Recursive.', name=__name__)
                self.recursive = True
            self.mp3s = self.get_mp3s_files()
            self.SongsData = meyed3.getMP3sTags(self.mp3s)
            self.answer = input("Do you want the data in Row or Column?(R/C): ")
            if self.answer == 'R' or self.answer == 'r':
                self.show_Tags_Row()
            elif self.answer == 'C' or self.answer == 'c':
                self.show_Tags_Column()
            self.main()

        elif self.answer == '4' or self.answer == '5':
            if self.answer == '5':
                self.recursive = True
            self.csv_filename = 'md3.csv'
            print("The CSV File Name : {} ? (y/n) : ".format(self.csv_filename))
            self.answer = self.getch()
            if self.answer == 'n':
                self.csv_filename = input("Enter Your CSV File Name : ")
            self.pf = ''.join((self.path, self.csv_filename))
            self.mp3s = self.get_mp3s_files()
            self.SongsData = meyed3.getMP3sTags(self.mp3s)
            self.saveCSVf()
            self.main()

        elif self.answer == '6' or self.answer == '7':
            if self.answer == '7':
                self.recursive = True
            self.json_filename = 'md3.json'
            print("The JSON File Name : {} ? (y/n) : ".format(self.json_filename))
            self.answer = self.getch()
            if self.answer == 'n':
                self.json_filename = input("Enter Your JSON File Name : ")
            self.pf = ''.join((self.path, self.json_filename))
            self.mp3s = self.get_mp3s_files()
            self.SongsData = meyed3.getMP3sTags(self.mp3s)
            self.saveJSONf()
            self.main()

        elif self.answer == '8'  or self.answer == '9':
            if self.answer == '9':
                self.recursive = True
            print("The CSV File Name : {} ? (y/n) : ".format(self.csv_filename))
            self.answer = self.getch()
            if self.answer == 'n':
                self.csv_filename = input("Enter Your CSV File Name : ")
            self.pf = ''.join((self.path, self.csv_filename))
            self.csvlist = self.readCSVf(self.pf)
            print('Tags of all mp3 in {} was Read.'.format(self.path))
            self.csvlist = self.correctPath(self)
            self.mp3s = self.splitCSVlist(self)
            meyed3.saveTagsFromCSV(self.pf)
            self.main()

        elif self.answer == '10':
            print("Rename {} file? (y/n) : ".format(self.audio_file))
            self.answer = self.getch()
            if self.answer == 'n':
                self.audio_file = ''
                self.audio_file = input("Enter Your Music File Name : ")
            self.audio_file = ''.join((self.path, self.audio_file))
            os.path.exists(self.audio_file)
            self.SongData = meyed3.get_Tags(self.audio_file)
            self.rename()
            self.main()

        elif self.answer == '11' or self.answer == '12':
            self.SongsData = ''
            if self.answer == '9':
                self.recursive = True
            self.mp3s = self.get_mp3s_files()
            self.SongsData = meyed3.getMP3sTags(self.mp3s)
            for self.SongData in self.SongsData:
                self.rename()
            self.main()
        
        elif self.answer == 'C':
            self.clear = lambda: os.system('clear')
            self.clear()
            self.main()

        elif self.answer == '0' or 'q':
            self.quit()
        self.quit()

if __name__ == '__main__':
    import datetime
    MD3.get_logger('Md3 Application Start Time :', name=__name__, create_file=True)
    start_time = datetime.datetime.now()
    sys.exit(mymd3=MD3(start_time, sys.argv))