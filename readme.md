# Finding_Scientific_Credibility
Finding Scientific Credibility of authors from Arnet-Miner Dataset.
This project uses tweepy to find number of followers from twitter and stores it in a file res.txt(run twit.py).
As Arnet-Miner datasets are huge, i have take only few entries.
main.py parses res.txt and gets followers, it then parses AMiner-Coauthor.txt and builds graph using networkx and 
also finds page-rank centrality.
The last step is to find kardashian index.
