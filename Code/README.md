## Here notes, suggestions and goals for each step of the code can be presented:

### General:
  The two codes (Part1, Part2) will be used only up to the generation of the adjacency matrices for the two scenarios (real network adn WS network) to study. Another code (Analysis.py) will be used for the analysis of these networks starting from the output data of the adjacency matrices produced in Part1,2.
  
  There is the possibility (only for part 2) to run several times the code with fixed parameters and extract network features (clustering coefficients, average distance..) from statistical significative samples.
  

#### Part 1:
  -  https://snap.stanford.edu/data/ca-GrQc.html dataset used. Note that:
        - Amount of nodes is different from the one actually reported in the page
        - Remapping of the dummy names given to authors was necessary in order to work with data (not necessarly true, we could have worked with indices directly, but it would have been more of a mess.
        - This specific dataset of collaborations was used as an entry test (the smallest in this scenario): larger dataset can be easily be used for later analysis.
        - Still in the original dataframe, there are 12 cases of authors which are "co-authors" with themselves: this can be explained with a possible error in the original dataframe OR co-authors having same surname, hence mapped to the same value.
        
  - http://www.cs.cmu.edu/~jure/pubs/powergrowth-tkdd.pdf look at referenced paper for discussing the dataset more properly
#### Part 2:
  
  - Use the .ipynb to use the code directly on jupyter (open code from Jupyter) or .py if you feel more like using other editors. 
  - The code will automatically create a /results_WS folder in which (both for pre and post rewiring) the adjacency matrices (.csv files) and plots of adjacency matrices and graphs will be saved. Name of each output file will include the parameters for the specific network simulated. Please try to keep the general architecture of the code in order to have it as versatile as possible : ) 
  - If once you have already executed the code it says "Creation of the directory /results_WS failed", don't worry: it's only because the folder is already there 
 - Up to now (23/11), output files with the same name will just be overwritten: if you want to have multiple output for the same parameters, consider making some changes in the output files names.
