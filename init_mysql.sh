mysql -uroot -e "create database qa";
mysql -uroot -e "create user 'ask-django'@'localhost' identified by '123'";
mysql -uroot -e "grant all on qa.* to 'ask-django'@'localhost'";
