# Project: Find the Path!

## Overview

In this project I practiced inheritance, graph search, and web
scraping, displaying my work in `scrape.py`.

`scrape.py` will has the following
* GraphSearcher (a class)
* MatrixSearcher (a class)
* FileSearcher (a class)
* WebSearcher (a class)
* reveal_secrets (a function)

Added a `bfs_search` to `GraphSearcher`.  It should behave the same as
`dfs_search`, but used the BFS algorithm instead of DFS.  The
difference was evident at the end if someone looks at the `.order`
attribute.

Note that without changing `MatrixSearcher`, it now supports both DFS
and BFS search since it inherits from `GraphSearcher`.

Added another class, `FileSearcher`, which also inherits from
`GraphSearcher`.  It has three methods (besides those
inherited): `__init__`, `go`, and `message`.

The nodes of this graph are files in the `file_nodes` directory. 

The `go` method reads a node file and return a list of children.
`go` will also record the values (1st lines) of the nodes that
are visited, in order.  The `message` method should return all the
values concatenated together.  Take a look at `bfs_test` in
`tester.py` for an example of how this should work.

 I scraped a website implemented as a web application built
using the flask framework. 

Used selenium to do the scraping. 
Treated each page as a node, and each hyperlink as a directed
edge. Implement the `go` method such that, each time a page is visited the table rows are appended to self.travelLog. 

Used inherited `dfs_search` method to return the DFS travel log (a data frame with rows ordered corresponding to the rows on the visited pages when performing a DFS). 

The method should navigate to the given URL, enter the password into
the keypad, click GO, and return a String identifying the current location. In addition, the method should scrape and download the image of the current location, saving it as 'Current_Location.jpg'. 

