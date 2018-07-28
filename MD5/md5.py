from hashlib import md5
import argparse
import time

#Encode function
def encode(hashObject, encoding='utf8'):
    return md5(hashObject.encode(encoding)).hexdigest()

#Decode function
def decode(hashObject,filepath):
    #Open a wordlist file with file path given by user
    try:
        file = open(filepath,"r")
    except Exception as e:
        print("ERROR: ",str(e))
        exit(1)

    start = time.time()#Starting time
    #Create loop to read all objects from a file which is given by user
    for object in file:
        #Hash the file objects
        fmd5 = md5(object.strip().encode(encoding='utf-8')).hexdigest()
        #Matching the hashed objects
        if hashObject == fmd5 :
            print("DECODED OBJECT: ", hashObject,"RESULT: ",object)
            break
    else:
        print("DID NOT FOUND IN YOUR WORD LIST!")
    end = time.time()#Ending time
    ctime = end - start#Total time
    print("TOTAL TIME: ",ctime," SECONDS\n")
    file.close()

#Main function
def Main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("-hs","--hashobject",help="use as : -hs [string] or --hashobject [string]",action="store")
    parser.add_argument("-p","--filepath",help="use as : -p [filepath] or --filepath [filepath]",action="store")
    group.add_argument("-e","--encode",help="use as:-hs [object] -e",action="store_true")
    group.add_argument("-d","--decode",help="use as: -hs [object] -p [path] -d",action="store_true")
    args = parser.parse_args()

    if args.encode:
        if args.hashobject:
            print('ENCODED OBJECT: ',encode(args.hashobject, encoding='utf8'))
    elif args.decode:
        if args.hashobject and args.filepath:
            decode(args.hashobject,args.filepath)
    else:
        print(parser.format_help())

if __name__ == '__main__':
    try:
        Main()
    except Exception as e:
        print('Something went wrong: ',str(e))
        exit(1)
