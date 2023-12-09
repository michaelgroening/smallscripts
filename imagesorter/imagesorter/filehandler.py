import os
import shutil
import filecmp
import hashlib

class FH(object):

    def __init__(self, src_filepath, dst_filepath):
        self.src_filepath=src_filepath
        self.dst_filepath=dst_filepath


    def scan_path(self):
        file_list = []
        self.recursive_filescan(file_list, self.src_filepath)
        for i in file_list:
            print(i)
        return file_list

    def recursive_filescan(self, file_list, dir):
        for root, d_names, f_names in os.walk(dir):
            for i in f_names:
                file_list.append(root + "/" + i)
            for j in d_names:
                self.recursive_filescan(file_list, j)

    def filter_suffixes(self, file_list, suffix_list):
        image_list=[]
        for file in file_list:
            splitted_file_name = file.split(".")
            if splitted_file_name[-1].lower() in suffix_list:
                image_list.append(file)
        return image_list

    def copy_file(self, file_vector):
        print("fooo")
        dst_path = "/".join([self.dst_filepath, file_vector[-1]])
        print(dst_path)
        if os.path.exists(dst_path):
            print("file exists")
            return
            if filecmp.cmp(file_vector[0],dst_path):
                print("same file")
                return
            else:
                hash = hashlib.md5(open(file_vector[0],'rb').read()).hexdigest()
                filename_split=dst_path.split(".")
                filename_split[-2]=filename_split[-2]+hash
                dst_path2=".".join(filename_split)
                os.makedirs(os.path.dirname(dst_path2), exist_ok=True)
                shutil.copy(file_vector[0], dst_path2)
                print(dst_path2)
                print("copying")
        else:
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.copy(file_vector[0], dst_path)
            print("copying")


    def move_file(self, file_vector):
        print("fooo")
        dst_path = "/".join([self.dst_filepath, file_vector[-1]])
        print(dst_path)
        if os.path.exists(dst_path):
            print("file exists")
            return
            if filecmp.cmp(file_vector[0],dst_path):
                print("same file")
                return
            else:
                hash = hashlib.md5(open(file_vector[0],'rb').read()).hexdigest()
                filename_split=dst_path.split(".")
                filename_split[-2]=filename_split[-2]+hash
                dst_path2=".".join(filename_split)
                os.makedirs(os.path.dirname(dst_path2), exist_ok=True)
                # shutil.copy(file_vector[0], dst_path2)
                shutil.move(file_vector[0], dst_path2)
                print(dst_path2)
                print("copying")
        else:
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            # shutil.copy(file_vector[0], dst_path)
            shutil.move(file_vector[0], dst_path)
            print("copying")
