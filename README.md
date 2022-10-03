# DFSBFS
DFS and BFS class using recursion

DFS: really fun recursion
BFS: really shouldn't have done recursion


BFS Original Algorithm:

    - create a universal queue with all nodes added to it ordered by layer sequentially
    - use a recursive method to stack each layer
        - iterate through each child node and add it to the list
        - in that iteration, call this method again to add children from current layer to the queue

    post condition: this implementation will automatically organize into a layer-based organized queue

I want to include my BFS pseudocode from my notebook because I thought it was rather complex 
and deviated heavily implementation-wise from my original plan. I think it transformed more into
a queue solution implemented through recursion which made the recursion somewhat unecessary, but I'm really glad
I explored this method. The problem with my original algorithm was that each iteration was organizing the nodes
by their respective children nodes rather than the entire layer, fragmenting the intended layer-based BFS organization 
