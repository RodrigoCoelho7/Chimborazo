def saveFile(filename,path,  lines):
    
    filename_compiled= str(filename).replace(".txt",".vm")
    f = open(path+filename_compiled,'w')

    f.writelines(lines)
    f.close()

    print("File saved: "+filename_compiled+" At: "+path)
