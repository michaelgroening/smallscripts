import exifread


class EH(object):

    def __init__(self, fh, images):
        self.filehandler = fh
        self.image_list = images
        # self.copy_map = []
        self.error_map = []

    def analyze_images(self):
        for image in self.image_list:
            #print(image)
            copy_vector = []
            splitted_file_name = image.split(".")
            filename = image.split("/")[-1]
            print(image)
            print(filename)
            if(filename[0]=="."):
                continue
            #if splitted_file_name[-1].lower() in ["srw"]:
            #    dst_path = "/".join(["SRW", filename])
            #    copy_vector.append([image, dst_path])
            #else:

            with open(image, 'rb') as image_file:
                try:
                    file_info = exifread.process_file(image_file, stop_tag='DateTimeOriginal', details=False)
                    creation_date = file_info['EXIF DateTimeOriginal'].printable
                    # my_image = Image(image_file)
                    # creation_date = my_image.get('datetime_original')
                    if creation_date:
                        filename = image.split("/")[-1]
                        dst_path = "/".join(
                            [
                                "/".join((creation_date.split(" ")[0]).split(":")),
                                filename
                            ]
                        )
                        copy_vector.append([image, dst_path])

                        #print(creation_date)
                    else:
                        filename = image.split("/")[-1]
                        dst_path = "/".join(["no_date", filename])
                        copy_vector.append([image, dst_path])
                except KeyError:
                    #print("Errror")
                    filename = image.split("/")[-1]
                    dst_path = "/".join(["error", filename])
                    copy_vector.append([image, dst_path])
                    #print("\n\n")
            #print(copy_vector[0])
            self.filehandler.move_file(copy_vector[0])


def copy_files(self):
    print("bar")
    for i in self.copy_map:
        self.filehandler.copy_file(i)
