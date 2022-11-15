# Commands
docker-comose up -d


# Create Super User
docker-compose run web python3.9 manage.py createsuperuser

# Make Migrations
docker-compose run web python3.9 manage.py makemigrations

# Make Migrations
docker-compose run web python3.9 manage.py migrate


#Run Test
docker-compose run web python3.9 manage.py test blog