# svg-network
Major research in the field of applying machine learning on vector images is largely non-existent. Whatever limited research is there, it's been done on hand-drawn data such as quickdraw dataset. 
Here we provide an alternative way to obtain noise free vector data of fonts. This code saves the vector path of the letter 'i' (ASCII 105) for different fonts. As of now, this can be changed by updating the fontforge command in main.py. Later, I'll add the functionality to extract other characters as well. 

Steps involved:
1. Install fontforge
2. Clone this github repository
3. Paste any number of fonts in svg-network/fonts folder
4. Run "python main.py" on your terminal from the svg-network directory
5. Run "python test.py" to see the results

