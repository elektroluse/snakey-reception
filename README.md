# snakey_reception

Containerized Django application, DRF API for user authentication. Sets HTTPOnly JWT cookies on login. Authenticated users can update or delete their own user. Produces a kafka message on sucessful user registration that can be consumed by any microservice subscribed to the topic `user_registered`. For example : [go-mailing](https://www.github.com/elektroluse/go-mailing).

No further functionality implemented as of now.


## Endpoints
- api/users/register `POST`
- api/users/login `POST`
- api/users/user-info `GET, PATCH, DELETE`



## Requirements
- [Docker/docker-compose](https://www.docker.com/)
- [make](https://www.gnu.org/software/make/) (optional)


## How to run
- `make dev`