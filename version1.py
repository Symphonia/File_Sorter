"""
###########################################################################
version: 1.1 experimental
Written in: Python 2.7.3
author: Kaze
date created: 1/20/2013
date edited : 1/21/2013
supported directory format:
    <full directory tree of sub directories regardless of level>
updated: recursive functions added
next update:
    <fine tune the getDirs() function>
future updates (not in order):
    1: allow for the option to compile mangas into volumes instead of
         one main folder
    2: after adding enough features -> export code to new file and
        clean up the code for more readability.
    3: selective copying -> specific the type of data <*.jpg, *.pdf>
        and copy the items with the type endings into new directory.
    4: allow for the option of either having the default new directory
        location or letting the user define their own path for the new
        directory.
usage: this program will take the contents of the old directory and then
move them into a new directory without subfolders
###########################################################################
"""
import os, sys, time
#global size limit symbolics
#the numerics are in bytes,
maxFileLoad = 1024*15000  #restrict max size limit to 15mb 
blockSize = 1024 * 5000   #will read 5mb at a time

#change the following constant values to change the behavior of the program
verbose = True
removeOldDirectory = False
fullDiveProtocol = True
selectiveCopying = False #to be implemented


#function for getting and testing directories
def getDirs():
    
    #check if the from directory is an actual directory
    while True:
        dirFrom = raw_input('enter input directory location: ')
        if not os.path.isdir(dirFrom):
            print'Error: the input directory is either:'
            print'not a directory or does not exist'
        else:
            break
    dirTo = dirFrom + '_compiled'
    #make new directory 
    if os.path.isdir(dirTo):
        dirTo = dirTo + '_copy'
        os.mkdir(dirTo)
    else:
        os.mkdir(dirTo)
    return (dirFrom,dirTo)

#version 1 method -> not longer needed -> use recursive function

#function for directory diving and getting the locations for the file 
#preferably for image or manga archive uses.
def dirDive(dirFrom,dirTo,verbose = verbose):
    #initialize file and directory counter  
    fileCount = dirCount = 0
    
    #first level directory : main folder
    for items in os.listdir(dirFrom):
        if os.path.isdir(os.path.join(dirFrom,items)):
            #second level directory: folder inside main folder (volume)
            dirCount+=1
            newDirList = os.listdir(os.path.join(dirFrom,items))
            newDir = os.path.join(dirFrom,items)
            for files in newDirList:
                if os.path.isdir(os.path.join(newDir,files)):
                    #third level directory: folder inside folder in main (chapter)
                    dirCount+=1
                    newDir2 = os.path.join(newDir,files)
                    newDirList2 = os.listdir(newDir2)
                    for files2 in newDirList2:
                        if os.path.isdir(os.path.join(newDir2,files2)):
                            #fourth level directory: folder inside chapter folder
                            dirCount+=1
                            newDir3 = os.path.join(newDir2,files2)
                            newDirList3 = os.listdir(newDir3)
                            for files3 in newDirList3:
                                pathFrom = os.path.join(newDir3,files3)
                                pathTo = os.path.join(dirTo,files3) 
                                if verbose == True:
                                    try:
                                        print 'file# ',fileCount
                                        print 'copying ', pathFrom,'to ',pathTo
                                        copyFile(pathFrom,pathTo)
                                        fileCount+=1
                                    except:
                                        print 'Error copying ', pathFrom,'to ', pathTo, '--skipped'
                                        print sys.exc_info()[0],sys.exc_info()[1]
                                else:
                                    try:
                                        copyFile(pathFrom,pathTo)
                                        fileCount += 1
                                    except:
                                        print 'Error copying ',pathFrom,'to ',pathTo,'--skipped'
                                        print sys.exc_info()[0],sys.exc_info()[1]                                  
                        pathFrom = os.path.join(newDir2,files2)
                        pathTo = os.path.join(dirTo,files2) 
                        if verbose == True:
                            try:
                                print 'file# ',fileCount
                                print 'copying ', pathFrom,'to ',pathTo
                                copyFile(pathFrom,pathTo)
                                fileCount+=1
                            except:
                                print 'Error copying ', pathFrom,'to ', pathTo, '--skipped'
                                print sys.exc_info()[0],sys.exc_info()[1]
                        else:
                            try:
                                copyFile(pathFrom,pathTo)
                                fileCount += 1
                            except:
                                print 'Error copying ',pathFrom,'to ',pathTo,'--skipped'
                                print sys.exc_info()[0],sys.exc_info()[1]           
                pathFrom = os.path.join(os.path.join(dirFrom,items),files)
                pathTo = os.path.join(dirTo,files)
                if verbose == True:
                    try:
                        print 'file# ',fileCount
                        print 'copying ', pathFrom,'to ',pathTo
                        copyFile(pathFrom,pathTo)
                        fileCount+=1
                    except:
                        print 'Error copying ', pathFrom,'to ', pathTo, '--skipped'
                        print sys.exc_info()[0],sys.exc_info()[1]
                else:
                    try:
                        copyFile(pathFrom,pathTo)
                        fileCount += 1
                    except:
                        print 'Error copying ',pathFrom,'to ',pathTo,'--skipped'
                        print sys.exc_info()[0],sys.exc_info()[1]
        else:            
            pathFrom = os.path.join(dirFrom,items)
            pathTo = os.path.join(dirTo,items)
            if verbose == True:
                try:
                    print 'file# ',fileCount
                    print 'copying ', pathFrom,'to ',pathTo
                    copyFile(pathFrom,pathTo)
                    fileCount+=1
                except:
                    print 'Error copying ', pathFrom,'to ', pathTo, '--skipped'
                    print sys.exc_info()[0],sys.exc_info()[1]
            else:
                try:
                    copyFile(pathFrom,pathTo)
                    fileCount += 1
                except:
                    print 'Error copying ',pathFrom,'to ',pathTo,'--skipped'
                    print sys.exc_info()[0],sys.exc_info()[1]
    return (fileCount,dirCount)


#function for displaying information and starting the copy file
##def dispInfo(dirFrom,item,files):
##     pathFrom = os.path.join(os.path.join(dirFrom,items),files)
##     pathTo = os.path.join(dirTo,files)
##        if verbose == True:
##            try:
##                print 'file# ',fileCount
##                print 'copying ', pathFrom,'to ',pathTo
##                copyFile(pathFrom,pathTo)
##                fileCount+=1
##            except:
##                print 'Error copying ', pathFrom,'to ', pathTo, '--skipped'
##                print sys.exc_info()[0],sys.exc_info()[1]
##        else:
##            try:
##                copyFile(pathFrom,pathTo)
##                fileCount += 1
##            except:
##                print 'Error copying ',pathFrom,'to ',pathTo,'--skipped'
##                print sys.exc_info()[0],sys.exc_info()[1]



#function for copying the files
#expanded to operate for bigger file sizes
def copyFile(pathFrom,pathTo,maxFileLoad = maxFileLoad):
    """
    copy one file pathFrom to pathTo, byte for byte
    uses binary file modes
    """
    chunksize = 0
    if os.path.getsize(pathFrom)<=maxFileLoad:
        #if file is less than 15mb
        #read the entire image file into memory
        fileFrom = open(pathFrom, 'rb')
        bytesFrom = fileFroms.read()
        #write all bytes into new file
        bytesTo = open(pathTo, 'wb')
        bytesTo.write(bytesFrom)
        #manual closure of file objects
        bytesFrom.close()
        byteTo.close()
    else:
        #if file is bigger than 15mb
        fileFrom = open(pathFrom,'rb')
        fileTo = open(pathTo,'wb')
        totalsize = os.path.getsize(pathFrom)
        while True:
            #reads the data from the original file 5mb at a time into the memory
            bytesFrom = fileFrom.read(blockSize)
            #when there is no more data comming in from the read(), break from while loop
            if not bytesFrom: break
            #copy the 5mb read into memory into the new file
            print 'nom nom nom...digesting byte chunks... ',100*(float(chunksize)/totalsize),'%'
            chunksize += blockSize
            fileTo.write(bytesFrom)
        print 'nom nom nom...digesting byte chunks... 100.0%'
        #manual closure of file objects
        fileFrom.close()
        fileTo.close()
            
#version 1 method-> no longer needed-> use recursive function 
#function for deleting the old directory
#follows the same path algorithm as dirTree, but instead of copying files
#it removes the files that were use to compile to the new directory
#for image folders only: preferably for manga archives
def removeOldDir(dirFrom):
    fileCount = dirCount = 0
    print 'starting removal of old directory \n'
    #will break the operation into 2 parts
    #first part will delete all files
    #second part wll delete the directories

    #firs part
    for items in os.listdir(dirFrom):
        if os.path.isdir(os.path.join(dirFrom,items)):
            #second level directory: folder inside main folder (volume)
            dirCount+=1
            newDirList = os.listdir(os.path.join(dirFrom,items))
            newDir = os.path.join(dirFrom,items)
            for files in newDirList:
                if os.path.isdir(os.path.join(newDir,files)):
                    #third level directory: folder inside folder in main (chapter)
                    dirCount+=1
                    newDir2 = os.path.join(newDir,files)
                    newDirList2 = os.listdir(newDir2)
                    for files2 in newDirList2:
                        if os.path.isdir(os.path.join(newDir2,files2)):
                            #fourth level directory: folder inside chapter folder
                            dirCount+=1
                            newDir3 = os.path.join(newDir2,files2)
                            newDirList3 = os.listdir(newDir3)
                            for files3 in newDirList3:
                                pathFrom = os.path.join(newDir3,files3)
                                if verbose == True:
                                    try:
                                        print 'file# ',fileCount
                                        print 'deleting ', pathFrom
                                        os.remove(pathFrom)
                                        fileCount+=1
                                    except:
                                        print 'Error deleting ', pathFrom,'--skipped'
                                        print sys.exc_info()[0],sys.exc_info()[1]
                                else:
                                    try:
                                        os.remove(pathFrom)
                                        fileCount += 1
                                    except:
                                        print 'Error deleting ',pathFrom,'--skipped'
                                        print sys.exc_info()[0],sys.exc_info()[1]
                        pathFrom = os.path.join(newDir2,files2)
                        if verbose == True:
                            try:
                                print 'file# ',fileCount
                                print 'deleting ', pathFrom
                                os.remove(pathFrom)
                                fileCount+=1
                            except:
                                print 'Error deleting ', pathFrom,'--skipped'
                                print sys.exc_info()[0],sys.exc_info()[1]
                        else:
                            try:
                                os.remove(pathFrom)
                                fileCount += 1
                            except:
                                print 'Error copying ',pathFrom,'--skipped'
                                print sys.exc_info()[0],sys.exc_info()[1]
                pathFrom = os.path.join(os.path.join(dirFrom,items),files)
                if verbose == True:
                    try:
                        print 'file# ',fileCount
                        print 'deleting ', pathFrom
                        os.remove(pathFrom)
                        fileCount+=1
                    except:
                        print 'Error deleting ', pathFrom,'--skipped'
                        print sys.exc_info()[0],sys.exc_info()[1]
                else:
                    try:
                        os.remove(pathFrom)
                        fileCount += 1
                    except:
                        print 'Error deleting ',pathFrom,'--skipped'
                        print sys.exc_info()[0],sys.exc_info()[1]
        else:
            pathFrom = os.path.join(dirFrom,items)
            if verbose == True:
                try:
                    print 'file# ',fileCount
                    print 'deleting ', pathFrom
                    os.remove(pathFrom)
                    fileCount+=1
                except:
                    print 'Error deleting ', pathFrom,'--skipped'
                    print sys.exc_info()[0],sys.exc_info()[1]
            else:
                try:
                    os.remove(pathFrom)
                    fileCount += 1
                except:
                    print 'Error deleting ',pathFrom,'--skipped'
                    print sys.exc_info()[0],sys.exc_info()[1]
    #second part
    for items in os.listdir(dirFrom):
        if os.path.isdir(os.path.join(dirFrom,items)):
            #second level directory: folder inside main folder (volume)
            dirCount+=1
            newDirList = os.listdir(os.path.join(dirFrom,items))
            newDir = os.path.join(dirFrom,items)
            for files in newDirList:
                if os.path.isdir(os.path.join(newDir,files)):
                    #third level directory: folder inside folder in main (chapter)
                    newDir2 = os.path.join(newDir,files)
                    newDirList2 = os.listdir(newDir2)
                    for files2 in newDirList2:
                        if os.path.isdir(os.path.join(newDir2,files2)):
                            #fourth level directory: folder inside chapter folder
                            try:
                                os.rmdir(os.path.join(newDir2,files2))
                                dirCount+=1
                            except:
                                print 'Error deleting ',os.path.join(newDir2,files2),'--skipped'
                                print sys.exc_info()[0],sys.exc_info()[1]
                    try:
                        os.rmdir(os.path.join(newDir,files))
                        dirCount+=1
                    except:
                        print 'Error deleting ',os.path.join(newDir,files),'--skipped'
                        print sys.exc_info()[0],sys.exc_info()[1]
            try:
                os.rmdir(os.path.join(dirFrom,items))
                dirCount+=1
            except:
                print 'Error deleting ',os.path.join(dirFrom,items),'--skipped'
                print sys.exc_info()[0],sys.exc_info()[1]
    try:
        os.rmdir(dirFrom)
        dirCount+=1
    except:
        print 'Error deleting ',dirFrom,'--skipped'
        print sys.exc_info()[0],sys.exc_info()[1]
    return (fileCount,dirCount)
    print 'old directory deleted\n'

#<full dir search>:recursive function
#<deep copy version>
def fullDirCopy(dirFrom,dirTo, verbose = verbose):
    fileCount = 0
    for filename in os.listdir(dirFrom):
        pathFrom = os.path.join(dirFrom,filename)
        pathTo = os.path.join(dirTo,filename)
        if not os.path.isdir(pathFrom): #if the tested file is not a directory
            if verbose == True:
                try:
                    print 'copying: ',pathFrom,' to ',pathTo
                    copyFile(pathFrom,pathTo)
                    fileCount +=1
                except:
                    print 'Error copying: ', pathFrom,' to ',pathTo,'--skipped'
                    print sys.exc_info()[0],sys.exc_info()[1]
            else:
                try:
                    copyFile(pathFrom,pathTo)
                    fileCount +=1
                except:
                    print 'Error copying: ',pathFrom,' to ',pathTo,'--skipped'
                    print sys.exc_info()[0].sys.exc_info()[1]
        else:
            try:
                subDirCounts = fullDirCopy(pathFrom,dirTo)
                fileCount += subDirCounts
            except:
                print 'Error Diving in directory through recursive dive'
                print 'Error directory: ',pathFrom
                print sys.exc_info()[0],sys.exc_info()[1]
    return (fileCount)

#<full dir search>:recursive function
#>deep remove version>
def fullDirRemove(dirFrom,verbose = verbose):
    fileCount = 0
    for filename in os.listdir(dirFrom):
        pathFrom = os.path.join(dirFrom,filename)
        if not os.path.isdir(pathFrom):
            if verbose == True:
                try:
                    print 'deleting: ',pathFrom
                    os.remove(pathFrom)
                    fileCount +=1
                except:
                    print 'Error deleting: ', pathFrom,'--skipped'
                    print sys.exc_info()[0],sys.exc_info()[1]
            else:
                try:
                    os.remove(pathFrom)
                    fileCount +=1
                except:
                    print 'Error deleting: ',pathFrom,'--skipped'
                    print sys.exc_info()[0].sys.exc_info()[1]
        else:
            try:
                subDirCounts = fullDirRemove(pathFrom)
                fileCount += subDirCounts[0]
            except:
                print 'Error Diving in directory through recursive dive'
                print 'Error directory: ',pathFrom
                print sys.exc_info()[0],sys.exc_info()[1]
    return (fileCount)

#recursive removal of directories
def fullDirDelete(dirFrom):
    for filename in os.listdir(dirFrom):
        pathFrom = os.path.join(dirFrom,filename)
        if os.path.isdir(pathFrom):
            if os.listdir(pathFrom)==[]:
                if verbose == True:
                    try:
                        print 'deleting: ',pathFrom
                        os.rmdir(pathFrom)
                    except:
                        print 'Error deleting: ', pathFrom,'--skipped'
                        print sys.exc_info()[0],sys.exc_info()[1]
                else:
                    try:
                        os.rmdir(pathFrom)
                    except:
                        print 'Error deleting: ',pathFrom,'--skipped'
                        print sys.exc_info()[0].sys.exc_info()[1]
            else:
                try:
                    fullDirDelete(pathFrom)
                except:
                    print 'Error Diving in directory through recursive dive'
                    print 'Error directory: ',pathFrom
                    print sys.exc_info()[0],sys.exc_info()[1]
    if not os.listdir(dirFrom)==[]:
        fullDirDelete(dirFrom)
    else:
        os.rmdir(dirFrom)
        print 'original directory deleted...'

    
def main():
    while True:
        dirTuple = getDirs()
        if dirTuple:
            print 'starting... \n'
            start = time.clock()
            if fullDiveProtocol == True:
                counts = fullDirCopy(*dirTuple)
                if removeOldDirectory==True:
                    delcounts = fullDirRemove(dirTuple[0])
                    fullDirDelete(dirTuple[0])
                    print 'deleted: ','files: ',delcounts
                print'copied: ','files: ',counts
            else:
                counts = dirDove(*dirTuple)
                if removeOldDirectory == True:
                    delcounts = removeOldDir(dirTuple[0])
                    print 'deleted: ','files: ',delcounts[0],' directories: ',delcounts[1]
                print'copied: ','files: ',counts[0],' directories: ',counts[1]
            print 'in ',time.clock() - start, ' seconds'
            looper = raw_input('continue? (q to quit)')
            if looper == 'q': break
    return 0

if __name__ == '__main__':
    main()
