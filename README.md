# JokerCore
A cool little project that guesses your cmd, or word. Play around with the filter algorithm constants. 
##Terms of Use
Please don't steal and use this for anything that is not opensource. Modules can be used if the project is opensource. 
##Algorithm Explanation:
<ol><b>Terms to know:</b>
  <li>Word tree: Sorted Tree of words. </li>
  <li>Search net: algorithm used to search the word tree.</li>
  <li>sortable_score: Score that determines how the word tree is sorted. It can make the search net search in very 
  different ways.</li>
  <li>net: The list of words that are found similar enough to be returned as the "net".</li>
  <li>Casting net: When the search net starts actually trying to add to the net.</li>
  <li>percent_rang: A param for the search net. Think of it as the net's whole width, so it determines how big the fish as to be to get caught. But it also determines when the search will start casting its net. </li>
  <li>look_range: A param for the search net. Think of it as the net's length. So it is how many levels in the word tree
  that will be looked at after the net has been cast.</li>
  <li>filter: For this a filter is what uses the net from the word tree, and filters out what is probably the word or cmd being looked for.</li>
  <li>common_score: A score based off the length of the string and the commonness of each letter.</li>
</ol>

The search net can be changed to go for full correctness and stop there, when using the sortable_score that uses
the full letter common_score. Beware using the wrong sortable_score with a small net because it will most likely
not find the word, even with correct spelling. The algorithm when using sortable_score with restricted common_score components
will try and fill the search net with similar words but if the inputted percent_range is too low it will not add any, 
leaving nothing in the net. It demonstrates a very straight forward thing: When guessing, ultimately, you will get the wrong thing
if you search to little, but when guessing with little doubt you will most certainly get your searched item. One of the sortable_scores
uses a large but fast guessing strategy, so the search net would have to be larger to get the searched item. When using the slower and
better guessing strategy, the search net can be very small and will most likely find the searched item. 
####A little on unique but similar data
As I experienced with trying to fit in thousands or millions of data into a data organization that requires unique values, there is overlap. So in my case if you had a lot of three letter words like 26 * 26 * 26 = 17,576, there is most likely going to be overlap in values. So my sortable score was allowing the data to rewrite placeholders. This is interesting, and important, in my case it worked in my favor to have groups of words, but in other cases it would not. So then starts the question how do you make a system that had a unique value for all of them. To make the question a little bit more difficult is this, "how do you make misspelling align as a similar word." Answering that is a little tricky I think, but try this: First you need a more complex way of comparing a string then this one int score, but you still need to keep it fast because, this is after all for big datasets. You need something like a double value, store the first portion 0 to infinity and keep comparing them that way. But to solve the uniqueness problem possibly start making a UUID from 0.0X (X being where the first UUID number goes), that way it does not interfere with the int compare but you keep a nice non-conflicting dataset. There you go a pretty easy way of storing strings uniquely but with aligning them to be easily compared to misspelled versions. 
####Future updates
I plan to add some optimization/options for the way things are <b>indexed</b> and how they are <b>searched</b> and <b>filtered</b>(The big three). A very cool thing would also be to build a web crawler that <b>dynamically changes the common_score</b>, with letter commonness but also word commonness. Another thing I plan to do is update the cmd portion of main to be an API so to allow people to use it for cmd searching. One last thing is that, at current, the indexing and searching is not very scalable to large data sets, I want to add an optimized form of the algorithms. 


