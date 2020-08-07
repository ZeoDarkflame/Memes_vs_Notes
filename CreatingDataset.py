import numpy as np
import cv2 as cv
import os

notes_list = []
memes_list = []

i = 0
notes = os.listdir('Notes')
os.chdir('Notes')

print('Processing Notes')
for note in notes:
    img = cv.imread(note)
    img = cv.resize(img,(256,256))
    print('on '+str(i),end='\r')
    notes_list.append(np.copy(img))
    i += 1
print('Completed Processing Notes')

notes_array = np.array(notes_list)
del notes_list,img
os.chdir('..')

i = 0
memes = os.listdir('Memes')
os.chdir('Memes')

print('Processing Memes')
for meme in memes:
    img = cv.imread(meme)
    img = cv.resize(img,(256,256))
    print('on'+str(i),end='\r')
    memes_list.append(np.copy(img))
    i += 1
print('Completed Processing Memes')

memes_array = np.array(memes_list)
del memes_list,img
os.chdir('..')

notes_labels = np.ones(notes_array.shape[0])
memes_labels = np.zeros(memes_array.shape[0])

X = np.concatenate((notes_array,memes_array))
Y = np.concatenate((notes_labels,memes_labels))

np.random.seed(0)
np.random.shuffle(X)
np.random.seed(0)
np.random.shuffle(Y)
print(X.shape)
print(Y.shape)

np.save('MVN_X.npy',X)
np.save('MVN_Y.npy',Y)