# DB Connection

This project have the goals simplify the SGDB connection for Python projects. 
You can get the source by: [Github-ConnectionDB](https://github.com/MVCompany/python/tree/master/ConnectionDb)
to write your content.

Package: ../python.exe setup.py sdist bdist_wheel
Add Rep: python.exe" -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
Rep: https://test.pypi.org/manage/project/connectiondb
References:
	package: https://packaging.python.org/tutorials/packaging-projects/
	

That project was write using anaconda, eclipse, and for this version, mongoDB.
	** Anaconda: 3-5.2.0
	** Eclipse: Oxygen.1a Release (4.7.1a)
	** MongoDB: 4.0.0
	
For using eclipse with anaconda a python used the references:
		https://quantitativenotes.wordpress.com/2013/07/31/how-to-upgrade-anaconda-to-python-3-3-and-use-in-eclipse-windows/ (http://docs.continuum.io/conda/intro.html)
		Install the python version using the anaconda cmd: conda create -n py35 python=3.5 anaconda
		Define the interpreter on the eclipse: $anaconda_home/envs/py35
		
For using MongoDB install in the python.exe -u pip install pymongo.
	(c:\ProgramData\Anaconda3\envs\py35>python.exe -m pip install pymongo)