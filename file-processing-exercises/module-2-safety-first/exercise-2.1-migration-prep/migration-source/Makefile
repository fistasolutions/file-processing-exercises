.PHONY: etl report clean

etl:
	python scripts/etl_pipeline.py

report:
	bash scripts/generate_report.sh

clean:
	rm -f data/processed_*.json
	rm -f reports/monthly-*.md
