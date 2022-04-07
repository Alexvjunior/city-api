run-postgres:
	docker start city-api-postgres 2>/dev/null || docker run --name city-api-postgres -p 5432:5432 -e POSTGRES_PASSWORD='postgres' -d postgres:10-alpine

check:
	pytest -vv -x --cov=apps --cov-report html:coverage --cov-fail-under=99


run:
	docker-compose up -d