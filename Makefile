lint:
	black --check kv_benchmark.py build_readme.py tests
	flake8 kv_benchmark.py tests build_readme.py

lint-fix:
	black tests kv_benchmark.py build_readme.py
	isort --profile=black tests kv_benchmark.py build_readme.py
	autoflake8 -i -r tests kv_benchmark.py build_readme.py

generate:
	rm -rf .benchmarks results
	mkdir -p results
	pytest --benchmark-warmup=on --benchmark-save=kv --benchmark-histogram=results/benchmark
	pytest-benchmark compare 0001 --columns="min,max,mean,rounds,ops" > results/table.txt
	python build_readme.py
