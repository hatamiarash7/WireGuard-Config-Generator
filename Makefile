clean: ## Clean config files
	rm -f *.conf

run: clean ## Run the script
	python3 main.py

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: clean run help
.DEFAULT_GOAL := help