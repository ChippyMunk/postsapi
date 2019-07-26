This application consists of a basic backend JSON API, which takes in query tags from users and returns a list of posts in json format. This API communicates with an external API from XXXX to get the posts source data. Please note that in the query string parameters, tags is required, while sortBy and direction are optional. Without specifying the sortBy and direction parameters, the results will be sorted by the post id in ascending order.<br />


This application is developed based on Python2.7, and requires pre-installation of the following dependencies: Falsk, requests and requests_cache.  
To install the dependencies, simply run these commands in your terminal of choice:  
<pre><code>pip install Flask</code></pre>  
<pre><code>pip install requests</code></pre>
<pre><code>pip install requests_cache</code></pre>

To start the application, please use the following command:  
<pre><code>python api.py</code></pre><br />

P.S. External api name and address are removed at request.
