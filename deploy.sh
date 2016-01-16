source ../bin/activate
sudo service apache2 stop
./update_dependencies.sh
mv ./logs/log.log ./logs/log.log.temp
touch ./logs/log.log
git pull
./manage.py makemigrations
./manage.py migrate
./manage.py syncdb
mv ./logs/log.log ./logs/deploy.log
mv ./logs/log.log.temp ./logs/log.log
sudo service apache2 start
deactivate
