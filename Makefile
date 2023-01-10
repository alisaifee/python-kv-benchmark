lint:
	black --check kv_benchmark tests 
	flake8 kv_benchmark tests

lint-fix:
	black tests kv_benchmark
	isort --profile=black tests kv_benchmark
	autoflake8 -i -r tests kv_benchmark

generate:
	rm -rf .benchmarks results
	mkdir -p results
	pytest --benchmark-save=kv --benchmark-histogram=results/benchmark
	pytest-benchmark compare 0001 --columns="min,max,mean,rounds,ops" > results/table.txt
	python build_readme.py
