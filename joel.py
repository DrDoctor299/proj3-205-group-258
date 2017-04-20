from py_ms_cognitive import PyMsCognitiveWebSearch

print("Please enter the word you wish to find the definition for: ")
t='definition'
##This asks the user for the word they wish 
user_input=input() 
user_input1=user_input+t
##This will search using the websearch function for the definiton of the word
word_search = PyMsCognitiveWebSearch('3d2f4008e4f8429fba7dccb98e855743',user_input)
##This will get the results from the search and save it into word_result
##word_result = word_search.search(limit=200)
## This will get the url and save it into definition with a limit of 200 links
definition = word_search.search(limit=200)
##This will print the first link containing the definition of the word
print("The definition of " + user_input)
print(definition[0].url)
# This will print the second link containing the definition of the word incase the first wasnt useful
print("The definition of  " + user_input)
print(definition[1].url)

