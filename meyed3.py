#!/usr/bin/env python3

import eyed3, md3

#eyed3.log.setLevel("ERROR")
def __init__():
    __csvlist = ''
    __SongsData = ''
    __dir = ''

def getMD5Hash(self, tag):
    key = '%s\t%s' % (tag.artist, tag.album)
    key = key.encode('utf-8')
    md5 = hashlib.md5()
    md5.update(key)
    return md5.hexdigest()

def emptyTag(self, audiofile):
    genre = 'Persian'
    comments = "WWW.AFW.IR : 1st Persian Audio Metadata Database"

def embed_album_art(self, mp3_file, artwork_file, artist, item_title):
    #### TODO
    ## NOT WORKING
    #edit the ID3 tag to add the title, artist, artwork, date, and genre
    tag = eyed3.Tag()
    tag.link(mp3_file)
    tag.setVersion([2,3,0])
    tag.addImage(0x08, artwork_file)
    tag.setArtist(artist)
    tag.setDate(localtime().tm_year)
    tag.setTitle(item_title)
    tag.setGenre(u"Trance")
    tag.update()

def get_album_art(self, path, f):
    __audiofile = eyed3.core.load(f)
    for __img in __audiofile.tag.images:
        if __img.picture_type == 3:
            __fw = open("{0}{1}-{2}_{3}.jpg".format(
                        path, __audiofile.tag.artist,
                        __audiofile.tag.album, 'COVER_FRONT'), 'w+b')
            print(u"Writing image file: , {0}{1}-{2}_{3}.jpg".format(
                        path, __audiofile.tag.artist,
                        __audiofile.tag.album, 'COVER_FRONT'))
            __fw.write(__img.image_data)

def get_album_art2(self):
    FRONT_COVER = eyed3.id3.frames.ImageFrame.FRONT_COVER
    audiofile = eyed3.load("test.id3")
    IMAGES = audiofile.tag.images
    with open("./FRONT_COVER.jpg", "rb") as fp:
        IMAGES.set(FRONT_COVER, fp.read(), "img/jpg", u"")
    audiofile.tag.save(encoding='utf-8', version=eyed3.id3.ID3_V2_4)

def get_lyrics(self, filename):
    url = "http://www.azlyrics.com/lyrics/" + artist + "/" + song + ".html"
        # Getting Source and extracting lyrics
    text = urllib2.urlopen(url).read()
    where_start = text.find('<!-- start of lyrics -->')
    start = where_start + 26
    where_end = text.find('<!-- end of lyrics -->')
    end = where_end - 2
    lyrics = unicode(text[start:end].replace('<br />', ''), "UTF8")
    pass

def setTagVersion(self, f, ver):
    __audiofile = eyed3.core.load(f)
    if (__audiofile.tag == None):
        __audiofile.initTag()

    if ver == '2.4.0':
        __audiofile.tag.save(version=eyed3.id3.ID3_V2_4)
    if ver == '2.3.0':
        __audiofile.tag.save(version=eyed3.id3.ID3_V2_3)

    print(f, 'Tag Version Changed to ', ver)


def MP3_Tag(self, audiofiles, tag, searchStr):
    __counter = 0
    for __filename in audiofiles:
        __audiofile = eyed3.load(__filename)
        __genre = audiofile.tag.genre
        #searchstr = "[wWw.[a-zA-z0-9].[com|org|net]"(Path(mp3s).rglob('*.mp3'))
        #seaingenere = re.compile(str(genre))
        print(__filename)
        print(__seaingenere.findall(searchStr))
        __counter += 1
        print(u'Found '+str(__counter)+' Music File with www in Gener or In Coments.')

def get_Tags(f):
    import time, os
    #get_logger('MD3Logger Start Get all Metadata of MP3 file', 'MD3Logger', 'DEBUG')

    #print(u'{}'.format(f.encode('utf-8', 'surrogateescape')))
    #print(f)

    try:
        __tags = eyed3.core.load(f)
    except OSError as err:
        print(u"OS Error: {}".format(err))
        return(False)
    except FileNotFoundError as fnferr:
        print(u'File Not found: {}'.format('fnferr'))
        return(False)

    __path =''.join((os.path.dirname(f), '/'))
    __mtime = time.strftime("%Y/%m/%d %a - %H:%M:%S", time.localtime(
                os.path.getmtime(f)))
    __ctime = time.strftime("%Y/%m/%d %a - %H:%M:%S", time.localtime(
                os.path.getctime(f)))
    try:
        __id3version = str(__tags.tag.version[0]) + '.' + str(__tags.tag.version[1])
    except AttributeError as atterr:
        print('Attributr Error in file {}'.format(f))
        return('Error')

    if len(__tags.tag.comments) > 0:
        __comm = __tags.tag.comments[0].text
        __commlang = __tags.tag.comments[0].lang
    else:
        __comm = ''

    if len(__tags.tag.lyrics) > 0:
        __lyric = __tags.tag.lyrics[0].text
        __lyriclang = __tags.tag.lyrics[0].lang
    else:
        __lyric = ''

    __tags = [
        os.path.basename(f), __tags.tag.artist, __tags.tag.title,
        __tags.tag.album, __tags.tag.album_artist, __tags.tag.track_num[0],
        __tags.tag.track_num[1], __tags.tag.disc_num[0],
        __tags.tag.disc_num[1], __tags.tag.release_date,
        __tags.tag.genre, __comm, __tags.tag.publisher, __lyric, __id3version,
        __tags.tag.header.tag_size, os.path.getsize(f),
        os.path.dirname(f) + "/", os.path.splitext(f)[1],__mtime,
        __ctime, os.path.getsize(f)]

    __tags = removeNone(__tags)
    return __tags

def setAudioTags(f, tagName, tagText):
    __audiofile = eyed3.load(f)
    if (__audiofile.tag != None):
        __audiofile.initTag()
        print('MetaData of {} Was Writed'.format(f))

    __audiofile.tag.artist = ''

def removeNone(tags):
    #get_logger('MD3Logger Start Remove None Tags', 'MD3Logger', 'DEBUG')
    tags = list(map(str, tags))
    tags = [ __tag.replace('None', '') for __tag in tags ]
    return tags

def getMP3sTags(mp3s):
    #get_logger('MD3Logger Start Split MP3 files', 'MD3Logger', 'DEBUG')
    __SongsData = []

    for __f in mp3s:
        __tags = get_Tags(__f)
        __SongsData.append(__tags)
    return __SongsData

def readCSVf(pf):
    import csv
    print(u'Opening {} CSV MetaData File ',pf)
    #get_logger('MD3Logger Start Read CSV file', 'MD3Logger', 'DEBUG')
    with open(pf) as __csvfile:
        print('{} File Was Opened'.format(pf))
        __csvlist = csv.reader(__csvfile)
        return list(__csvlist)

def saveTagsFromCSV(pf):
    import os
    from collections import deque
    #get_logger('MD3Logger Start Save Tags in CSV file', 'MD3Logger', 'DEBUG')
    if os.path.isfile(pf):
        __csvlist = readCSVf(pf)
    else:
        print(u'There is no CSV file : !!!', pf)
        exit(1)

    __csvlist.pop(0)
    ## .popleft()
    for __row in __csvlist:
        __f = ''.join((__row[17], __row[0]))
        #print(__f)
        audiofile = eyed3.core.load(__f)
        if __row[1] is not None:
            audiofile.tag.artist = __row[1]
        if __row[2] is not None:
            audiofile.tag.title = __row[2]
        if __row[3] is not None:
            audiofile.tag.album = __row[3]
        if __row[4] is not None:
            audiofile.tag.album_artist = __row[4]
        if __row[5] != '':
            audiofile.tag.track_num = (int(__row[5]))
            if __row[5] and __row[6] != '':
                audiofile.tag.track_num = (int(__row[5]), int(__row[6]))
##        if __row[7] != '':
##            audiofile.tag.disc_num = (int(__row[7]))
##            if __row[7] and __row[8] != '':
##                audiofile.tag.disc_num = (int(__row[7]), int(__row(8)))
        if __row[9] is not None:
            audiofile.tag.release_date = __row[9]
        if __row[10] is not None:
            audiofile.tag.genre = __row[10]
        if __row[11] is not None:
            audiofile.tag.comments.set(__row[11])
        if __row[12] is not None:
            audiofile.tag.publisher = __row[12]
        if __row[13] is not None:
            audiofile.tag.lyrics.set(__row[13])
        audiofile.tag.save(version=(2, 3, 0))
        print('MetaData {}  Was Saved.'.format(pf))