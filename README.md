# BAEA
Basic A** Election Analaysis : Uses results from NYT to esitmate wins and losses of close races using standing county results ratios as a hueristic
<h2>This project was mostly made for quick result guessing during election week 2022 and is far from complete. </h2>

<h1> File Format Notes </h1>
<ul>
<li>
Files are sensitive to formatting
</li>
<li>
This uses results copied from the NYT ballot measures results page to estimate potential winners and losers of local (and often unforecasted) elections. 
</li> <li>
Counties that contain spaces will need to be manually formatted (for now) to include underscores. This is usually easy to do. A tool may be made for this. 
This is a current outstanding issue. 
</li>
</ul>
<h1>How To Use</h1>
<ul>
<li>
Run est.py, this will prompt you for a filepath to the file you'd like to analyze.
</li><li>
Again, make sure it is properly formatted. This may not work for all files. 
</li><li>
Warning: Right now, formatted names are only working for triple digit ballot measures and local filepaths. Some naming may look weird. I very much just threw this together as a side project and would like to reformat this code. 
</li>
</ul>




<h1>Here is a projection based off this project:</h1>

<img src="https://raw.githubusercontent.com/Dsrts-edu/BAEA/main/Estimator%20copy.jpg" width=100% height=100%>
