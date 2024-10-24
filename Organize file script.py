import os
import shutil
import speech_recognition as sr

# current directory we are working on
current_dir = 'C:\\Users\\maaz\\Downloads'
extension_map = {  
    '.jpg': 'Images',  
    '.png': 'Images',  
    '.gif': 'Images',  
    '.jpeg': 'Images',  
    '.avif': 'Images',  
    '.pdf': 'PDF Files',  
    '.txt': 'Text Files',  
    '.docx': 'Word Document',  
    '.xlsx': 'Excel Files',  
    '.pptx': 'PowerPoint Persentations',  
    '.ppt': 'PowerPoint Persentations',  
    '.mp3': 'Audio',  
    '.wav': 'Audio',  
    '.mp4': 'Video',  
    '.avi': 'Video',  
    '.exe': 'Executable Files',
    '.msi': 'Executable Files',
    '.py': 'Python Files',  
    '.cpp': 'C++ Files',  
    '.c': 'C Files',  
    '.java': 'Java Files',  
    '.html': 'HTML Files',  
    '.css': 'CSS Files',  
    '.js': 'Javascript Files',  
    '.zip': 'Zip_Files',
    '.xml': 'XML Files',
    '.torrent': 'Torrent Files',
    '.ini': 'ini Files',
    '.iso': 'ISO Files',
}  
def create_dir(dest_dir):
    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)
        
def move_files(filepath, dest_dir):
    shutil.move(filepath, os.path.join(dest_dir, os.path.basename(filepath)))
    
def organize_files(extention_filter= None):
    
    #loop through each file in the source
    for filename in os.listdir(current_dir):
        print(filename)
        #full path of each file
        filepath = os.path.join(current_dir, filename)
        if os.path.isfile(filepath):
            file_ext = os.path.splitext(filename)[-1].lower()
            #if we enter a specfic a ext it will match the extention_filter to file_ext and if ti does only those files will be sorted
            if extention_filter is None or file_ext == extention_filter:
                dest_dir = os.path.join(current_dir, extension_map[file_ext])
                create_dir(dest_dir) 
                #path of where we wanna move to our file
                dest_path = os.path.join(dest_dir, filename)
                #move the file to the destination dir
                move_files(filepath, dest_dir)
            else:
                print(f"Error: {filename}")



            
if __name__ == "__main__":
    organize_files()