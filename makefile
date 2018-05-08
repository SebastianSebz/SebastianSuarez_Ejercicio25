
Graph.png: planetas.txt graph.py
	python graph.py

planetas.txt: Planetas_prob.py
	python Planetas_prob.py > planetas.txt


