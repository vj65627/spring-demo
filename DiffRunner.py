__author__ = 'vj65627'
'''
>>>>10 April 2015
1. Read both the directory
2. Extract the packages into temp directory
3. compare the packages
4. generate diff report as html
5. email the diff report
'''
import sys,getopt,os,zipfile,tempfile

def main(argv):

# Code Snippet to read location of 2 directories as arguments
    newfile=""
    oldfile=""
    try:
        opts, args = getopt.getopt(argv, 'n:o:')
        if len(sys.argv) < 2:
            print('DiffRunner.py -n <new hand-off path> -o <old hand-off path>')
            sys.exit(2)
    except getopt.GetoptError:
        print('DiffRunner.py -n <new hand-off path> -o <old hand-off path>')
        sys.exit(2)
    else:
       # print(str(sys.argv))
        for opt, arg in opts:
            if len(sys.argv) == 5 and str(sys.argv[1]) =='-n' and str(sys.argv[3])=='-o':
                if opt in "-n":
                    newfile=str(sys.argv[2])
                if opt in "-o":
                    oldfile=str(sys.argv[4])
                    ArgumentValidator(newfile,oldfile)
            else:
                print('DiffRunner.py -n <new hand-off path> -o <old hand-off path>')
                sys.exit(2)

#Code Snippet to validate the arguments as directories plus not empty
def ArgumentValidator(NFvalue,OFvalue):
    if os.path.exists(NFvalue) and os.path.exists(OFvalue):
        if len(os.listdir(NFvalue))==0 or len(os.listdir(OFvalue))==0:
            print('DiffRunner.py: Either one (or) both the Argument Path is Empty')
            sys.exit(2)
        else:
            ContentExtractor(NFvalue,OFvalue)
    else:
        print('DiffRunner.py: Either one (or) both the Argument is not valid path')
        sys.exit(2)

#Code Snippet to Extract the directory contents into temporary location
def ContentExtractor(UnZipNFvalue,UnZipOFvalue):
    UnZipNFTempvalue=tempfile.mkdtemp(suffix='01', prefix='tmp', dir=None)
    UnZipOFTempvalue=tempfile.mkdtemp(suffix='02', prefix='tmp', dir=None)

    zip = zipfile.ZipFile(UnZipNFvalue)
    zip.extractall(path=UnZipNFTempvalue)

if __name__ == "__main__":
    main(sys.argv[1:5])
