from mutagen.id3 import ID3, TCON
import glob
import sys, os
import warnings

def main():
    dataDir = './'

    if (len(sys.argv) == 2):
        dataDir = sys.argv[1]       

        if (not os.path.isdir(dataDir)):
            warnings.warn(dataDir + ' is not vaild a directory')
            sys.exit()

        if dataDir[-1] != '/':
            dataDir += '/'

    elif (len(sys.argv) > 2):
        warnings.warn("Too many arguemnts")
        sys.exit()

    files = glob.glob(dataDir + '*/*.mp3')


    for file in files:
        print(file)
        filename = file.split('/')[-1]
        genre = file.split('/')[-2]

        tags = ID3(file)
        tags["TCON"] = TCON(encoding=3, text=genre)
        tags.save(file)

if __name__ == '__main__':
    main()
