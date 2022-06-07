clean:
	@find . -name "*.pyc" -delete
	@find . -name ".python-version" -delete
	@find . -name "__pycache__" -type d -delete
	@find . -name "exercicio.zip" -delete

compress: clean
	tar -czvf exercicios.zip exercicio_*

lint:
	flake8 --max-line-length 119 .
