    import sys
    import os
    import hashlib
    import shutil

    def chunk_reader(fobj, chunk_size=2048):
        """Generator that reads a file in chunks of bytes"""
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        return chunk

    def check_for_duplicates(paths, hash=hashlib.sha1):
        hashes = {}
        for path in paths:
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    full_path = os.path.join(dirpath, filename)
                    hashobj = hash()
                    chunk = chunk_reader(open(full_path, 'rb'))
                    hashobj.update(chunk)
                    file_id = (hashobj.digest(), os.path.getsize(full_path))
                    duplicate = hashes.get(file_id, None)
                    if duplicate:
                        print("Duplicate found: %s and %s" % (full_path, duplicate))
                        #try:
                        #	os.stat("duplicates/"+dirpath)
                        #except:
                        #	os.makedirs("duplicates/"+dirpath)
                        #shutil.move(full_path,"duplicates/"+full_path)
                    else:
                        hashes[file_id] = full_path

    if sys.argv[1:]:
        check_for_duplicates(sys.argv[1:])
    else:
        print ("Please pass the paths to check as parameters to the script")
