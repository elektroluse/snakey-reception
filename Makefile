
.PHONY: dev prod flush superuser

dev:
	@echo "bulding dev container"
	docker-compose -f docker-compose.dev.yml up --build
prod:
	@echo "Prod compose is not yet implemented"

flush:
	@echo "Flushing dev database"
	docker exec -it snakey_reception_dev python manage.py flush
superuser:
	@echo "Running createsuperuser"
	docker exec -it snakey_reception_dev python manage.py createsuperuser