# twrk-back

## Run project

1. Clone: `git clone git@github.com:odi1n/twrk-back.git`
2. Docker build: `docker-compose up --build`
3. Create user: `docker-compose exec web python manage.py createsuperuser --no-input`
4. User:
    1. email: `admin@admin.ru`
    2. username: `admin`
    3. password: `admin`

## Endpoint

Link page: `http://localhost:8000`

|Link|Infomation|Params|
|:---|:---|:---|
|/admin/|admin panel|-|
|/api/v1/|schema prodcuts|-|
|/api/v1/products/|list all products|search, status|
|/api/v1/products/:id/|get info products id|-|
