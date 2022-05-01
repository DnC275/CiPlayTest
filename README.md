# Statistics store
## Deployment
### Manually
```bash
python -m venv venv
source venv/bin/activate
pip install requirements.txt
```
Run postgres server and set the necessary environment variables in the .env file.
You can start postgres with docker by command:
```bash
docker-compose run -p 5432:5432 postgres
```
Apply migrations:
```bash
alembic upgrade head
```
Start app:
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
### Via docker:
```bash
docker-compose up
```
Application will be available on 0.0.0.0:8000
## Documentation
To get acquainted with the available methods, go to http://{app_host}:{app_port}/docs