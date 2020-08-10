# Memes_vs_Notes
All of us have thousands of pictures on our phones,   
two major contenders for storage space are Memes and Notes

## Creating Dataset
Keep the Creating Dataset Script in the same folder as Memes and Notes (named as 'Memes' and 'Notes' respectively) and run it.  
This will produce numpy arrays MVN_X.npy and MVN_Y.npy which are images and labels respectively.

## Architecture (Conv)
F - Filter, S - Stride, C - Channels   
Conv Layer - F(11x11) S(4x4) C(3,96)  
Conv Layer - F(5x5) S(4x4) C(96,134)  
Max Pool - F(2x2) S(2x2)   
Conv Layer - F(3x3) C(134,158)   
Max Pool - F(2x2) S(2x2)  
Dense - C(158x2x2,252)   
Dense - C(252,1)   

Optimizer - ADAM    
learning_rate = 0.001   
The Best dataset is saved as **MVN2.pth**  

**Accuracy**
Training Set (1500/1600) - 97.8%   
Test Set (100/1600) - 100%

## Architecture (Non-Conv)
Dense Layer - C(256x256x3,1000)   
Dense Layer - C(1000,50)  
Dense Layer - C(50,1)   

Optimizer - ADAM
learning_rate = 0.001  

**Accuracy**
Training Set (1500/1600) - 88.26%  
Test Set (100/1600) - 88%

## Data
Data is at
https://drive.google.com/drive/folders/1SH5Y8fpwue2uIN1kOeyj_HweW4AP1xKO?usp=sharing   
paste MVN_X.npy and MVN_Y.npy in the data folder

## To open the Colab Notebooks
Goto - https://colab.research.google.com/github/
and then copy and paste the notebook links from the repository
