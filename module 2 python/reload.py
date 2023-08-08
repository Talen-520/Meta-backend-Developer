import importlib
#import sample #loaded and excute first hello world
import file_changes
#importlib.reload(sample)

def changes():
    try:
        importlib.reload(file_changes)
        file_changes.print_changes()
    except:
        pass
for i in range(5):
    changes()
    input("Hit enter to continue...")


#the reload function can be used for making dynamic changes within your code with the help of import statements.