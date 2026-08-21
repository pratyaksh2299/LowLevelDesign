from abc import ABC, abstractmethod
from logging import root
from typing import List
# base component
class FileSystem(ABC):

    @abstractmethod
    def display(self,indent=0):
        pass

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def delete(self):
        pass

# leaf component

class File(FileSystem):

    def __init__(self,name,size):
        self.name = name
        self.size = size

    def display(self,indent=0):
        print(' ' * indent+f'File:{self.name}, Size: {self.size}')
    
    def get_size(self):
        return self.size

    def delete(self):
        print(f'File deleted: {self.name}')


# composite component
class Directory(FileSystem):

    def __init__(self,name):
        self.name = name
        self.children : List[FileSystem] = []

    def add(self,child):
        self.children.append(child)

    def remove(self,child):
        self.children.remove(child)

    def display(self,indent=0):
        print(' ' * indent+f'Directory:{self.name}')
        for child in self.children:
            child.display(indent+2)

    def get_size(self):
        total_size =0
        for child in self.children:
            total_size += child.get_size()
        return total_size

    def delete(self):
        print(f'Directory deleted: {self.name}')
        # Delete children first
        for child in self.children:
            child.delete()
        # Clear children list
        self.children.clear()

            
if __name__ == '__main__':
    file1 = File('file1.txt', 100)
    file2 = File('file2.txt', 200)
    file3 = File('image.png', 500)
    file4 = File('video.mp4', 1000)
    dir1 = Directory('Documents')
    dir1.add(file1)
    dir1.add(file2)
    dir2 = Directory('Media')
    dir2.add(file3)
    dir2.add(file4)
    root_dir = Directory('Root')
    root_dir.add(dir1)
    root_dir.add(dir2)
    root_dir.display()

    # Get the total size of the root directory
    print(f'Total size of root directory: {root_dir.get_size()}')

    # Delete media directory
    root_dir.remove(dir2)
    print('After deleting Media directory:')
    root_dir.display()
