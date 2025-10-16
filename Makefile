
.PHONY: dev prod

dev:
	@echo "bulding dev container"
	docker-compose -f docker-compose.dev.yml up --build
prod:
	@echo "Prod compose is not yet implemented"