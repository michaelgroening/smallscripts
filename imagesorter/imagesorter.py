from imagesorter import filehandler
from imagesorter import exifhandler


def main():
    print("Hello World!")
    FH = filehandler.FH("./Amazon Photos-Downloads", "./out")
    file_list = FH.scan_path()
    images = FH.filter_suffixes(file_list, ["jpg","jpeg","srw","dng","tif","tiff","png","dng","PNG","DNG"])
    #for i in images:
    #    print(i)
    EH = exifhandler.EH(FH, images)
    EH.analyze_images()
    #EH.copy_files()
    #EH.copy_files()


if __name__ == "__main__":
    # execute only if run as a script
    main()
