import os 


#path FOR ALL OUR FILES 

WORK-DIR_path = 'work-DIR'
record_path = 'work-DIR\records'





#Create Label Map
labels = [
        {'name':'A', 'id':1}, 
        {'name':'B', 'id':2},
        {'name':'C', 'id':3},
        {'name':'D', 'id':4},
        {'name':'Thanks', 'id':5},
]

with open(ANNOTATION_PATH + '\label_map.pbtxt', 'w') as f:
    for label in labels:
        f.write('item { \n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')
