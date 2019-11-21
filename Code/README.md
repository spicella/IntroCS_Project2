## Here notes, suggestions and goals for each step of the code can be presented:

#### Part 1:
  -  https://snap.stanford.edu/data/ca-GrQc.html dataset used. Note that:
        - Amount of nodes is different from the one actually reported in the page
        - Remapping of the dummy names given to authors was necessary in order to work with data (not necessarly true, we could have worked with indices directly, but it would have been more of a mess.
        - This specific dataset of collaborations was used as an entry test (the smallest in this scenario): larger dataset can be easily be used for later analysis.
        - Still in the original dataframe, there are 12 cases of authors which are "co-authors" with themselves: this can be explained with a possible error in the original dataframe OR co-authors having same surname, hence mapped to the same value.
        
  - http://www.cs.cmu.edu/~jure/pubs/powergrowth-tkdd.pdf look at referenced paper for discussing the dataset more properly
#### Part 2:
  
