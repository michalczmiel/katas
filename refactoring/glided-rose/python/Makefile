.PHONY: test
test:
	pytest --cov=glided_rose test_glided_rose.py

.PHONY: typecheck
typecheck:
	mypy glided_rose.py

.PHONY: metrics-cc
metrics-cc:
	echo "Cyclomatic Complexity"
	radon cc glided_rose_legacy.py glided_rose.py

.PHONY: metrics-hal
metrics-hal:
	echo "Halstead Metrics"
	radon hal glided_rose_legacy.py glided_rose.py

.PHONY: metrics
metrics: metrics-cc metrics-hal
