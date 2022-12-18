import os
# os.chdir(path) # changing to a directory
# os.listdir() # listdir objects from directory
# os.getcwd() # returns current working directory
# os.rename('old_name.ext','new_name.ext')# to rename

# os.rmdir('dir_name/sub_dir_name') # remove 1 folder, the final one
# os.removedirs('dir_name/sub_dir_name')# remove all folder in between

# os.mkdir('dir_name') # to make a directory
# os.makekdirs('dir_name/sub_dir_name')# this will create all dir tree for you

# os.stat('file_name') # if printed you get info from file
# -os.stat('text.txt').st_size # size of the file
# -os.stat('text.txt').st_mtime # returns created time as a time
#       stamp-> importdatetime: print(datetime.fromtimestamp(mod_time))

# os.walk()
# for dirpath, dirname, filenames in os.walk('path from top to bottom')
#     print('curretn:', dirpath)
#     print('dirname:', dirname)
#     print('filenames:', filenames)#

# home_path = os.eviron.get('Home')
# filepath = os.path.join('home_path','test.txt')# to create a save path

# os.path.basename('/tmp/test.txt') # returns the file name
# os.path.dirname('/tmp/test.txt') # returns the dir name
# os.path.split('/tmp/test.txt') # returns the dir and file name

# os.path.exists('/tmp/test.txt') # true or false
# os.path.isDir('/tmp/test.txt') # true or false
# os.path.isFile('/tmp/test.txt') # true or false

# for item  in os.environ:
#     print(item)

username = os.environ.get("USERNAME")

print(username)