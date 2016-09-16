# JokerCore
A cool little project that guesses your cmd, or word. Play around with the filter algorithm constants. 
##Terms of Use
Please don't steal and use this for anything that is not opensource. Modules can be used if the project is opensource. 
##Algorithm Explanation:
<ol><b>Terms to know:</b>
  <li>Word tree: Sorted Tree of words. </li>
  <li>Search net: algorithm used to search the word tree.</li>
  <li>sortable_score: Score that determins how the word tree is sorted. It can make the search net search in very 
  different ways.</li>
  <li>net: The list of words that are found similar enought to be returned as the "net".</li>
  <li>Casting net: When the search net starts actually trying to add to the net.</li>
  <li>percent_rang: A param for the search net. Think of it as the net's whole width, so it determins how big the fish as to be to get caught. But it also determins when the search will start casting its net. </li>
  <li>look_range: A param for the search net. Think of it as the net's length. So it is how many levels in the word tree
  that will be looked at after the net has been cast.</li>
  <li>filter: For this a filter is what uses the net from the word tree, and filters out what is probably the word or cmd being looked for.</li>
  <li>common_score: A score based off the length of the string and the commoness of each letter.</li>
</ol>

The search net can be changed to go for full correctness and stop there, when using the sortable_score that uses
the full letter common_score. Beware using the wrong sortable_score with a small net becasue it will most likely
not find the word, even with correct spelling. The algorithm when using sortable_score with restricted common_score components
will try and fill the search net with similar words but if the inputed percent_range is too low it will not add any, 
leaving nothing in the net. It demonstrates a very straight forward thing: When guessing, ultimitely, you will get the wrong thing
if you search to little, but when guessing with little doubt you will most certinly get your searched item. One of the sortable_scores
uses a large but fast guessing strategy, so the search net would have to be larger to get the searched item. When using the slower and
better guessing strategy, the search net can be very small and will most likely find the searched item. 

####Future updates
I plan to add some optimization/options for the way things are <b>indexed</b> and how they are <b>searched</b> and <b>filtered</b>(The big three). A very cool thing would also be to build a webcrawler that <b>dynamically changes the common_score</b>, whith letter commonness but also word commomness. Another thing I plan to do is update the cmd portion of main to be an API so to allow people to use it for cmd searching. One last thing is that, at current, the indexing and searching is not very scalable to large data sets, I want to add an optimized form of the algorithms. 
