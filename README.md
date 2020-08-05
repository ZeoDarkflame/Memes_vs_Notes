# Memes_vs_Notes
*Detecting whether a given image is a meme or notes*

## Architecture
Conv Layer - F(11x11) S(4x4) C(3,96)  
Conv Layer - F(5x5) S(4x4) C(96,134)  
Max Pool - F(2x2) S(2x2)   
Conv Layer - F(3x3) C(134,158)   
Max Pool - F(2x2) S(2x2)  
Dense - C(158x2x2,252)   
Dense - C(252,1)   

Optimizer - ADAM    
learning_rate = 0.001
