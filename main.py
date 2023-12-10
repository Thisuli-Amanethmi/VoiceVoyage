#import pandas as pd


# Metadata DataFrames
# 13 objects
metadata1 = ({
    'ID': [1,2,3,4,5,6,7,8,9,10,11,12,13],
    'Label': ['Wall','Chair','Table','Sofa','TV','Door','Window','Bed','Cupboard','DressingTable','Commode','Sink','Fridge'],
    'File_Path':['']
})
# Staircase
metadata2 = ({
    'ID': [14],
    'Label': ['Staircase'],
    'File_Path':['']
})
# Washing Machine
metadata3 = ({
    'ID': [15],
    'Label': ['WashingMachine'],
    'File_Path':['']
})
# Stove cooker
metadata4 = ({
    'ID': [16],
    'Label': ['Cooker'],
    'File_Path':['']
})
# Dustbin
metadata5 = ({
    'ID': [17],
    'Label': ['Dustbin'],
    'File_Path':['']
})
# Broom
metadata6 = ({
    'ID': [18],
    'Label': ['Broom'],
    'File_Path':['']
})

# Accessing metadata for the first image
#first_image_metadata1 = metadata1[0]
#first_image_metadata2 = metadata2[0]
#first_image_metadata3 = metadata3[0]
#first_image_metadata4 = metadata4[0]
#first_image_metadata5 = metadata5[0]
#first_image_metadata6 = metadata6[0]

#print(first_image_metadata1)


# Staircase
#metadata2 = pd.DataFrame({
    #'ID': [14],
    #'Label': ['Staircase'],
    #'File_Path':['']
#})
# Merge metadata based on the 'ID' column
#combined_metadata = pd.merge(metadata1, metadata2, metadata3, metadata4, metadata5, metadata6, on='ID', how='outer')


