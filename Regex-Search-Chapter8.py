import re
folder = r'C:\Users\Luiz\Desktop\teste' # folder directory
try:
    file = open("{}.txt".format(folder))
    search = input('Enter with your search: ')
    reg_exp = re.compile(r"{}".format(search), re.I)
    mo = reg_exp.search(file.read())
    print('Found:')
    print(mo.group())
    file.close()
except:
    print('The file does not exist or search not found! Try again')
