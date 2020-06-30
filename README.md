# TRIE-Data-Structure-in-Python
Implementation of TRIE data structure in Python language.

TRIE data structure is a Tree based structure for prefix matching in strings. It can be used in implementation of a dictionary where the Key is the stored in the TRIE structure and the ending node stores the value corresponding the the key.  

More information about the TRIE data Structure can be found here:
https://www.geeksforgeeks.org/trie-insert-and-search/
https://en.wikipedia.org/wiki/Trie

  The project made on an Example case of the large scale Data Forms where navigation to next required field is very difficult when all the field donot have to be filled. 
  
  Consider a case where the a large data form exists and the user only has to fill a limited number of enteries at a time. Pressing TAB key usually switches cursor to the next field. But in cases when a lot of fields are unnecessary the user has to go through all those fields.
  
  We implement a TRIE structure solution that can be used on the backend of the TAB key press event. We assume that the company has the data of the behaviour of the form user that the user navigates to which field more after each field filled. We certainly didnt have any such kind of DATA so we made a data generating script. 

## Data generating script
The script generates a list of number of keyfields that may have been traversed in a form filling with some probability constraints.  
The Data is generated in variable sizes.

## The script 
The script runs and generates a TRIE data structure based on the form filling data. now we can use this TRIE in the production env. and program it accordingly while in the form filling work, the use of TAB key press(or any other shortcut) can shift us to the most frequently used form field based on the probability of the TRIE tree. 
