#!/bin/sh
echo "------------------------"
echo "-- POSTGRES -INI- --"
echo "------------------------"
cd /
./wait-for-it.sh db:5432 -t 0 -- echo "postgres is up"
echo "------------------------"
echo "-- POSTGRES -FIN- --"
echo "------------------------"

cd /api

echo "------------------------"
echo "-- REQUIREMENTS -INI- --"
echo "------------------------"
pip install -r requirements.txt
echo "------------------------"
echo "-- REQUIREMENTS -FIN- --"
echo "------------------------"

echo "------------------------"
echo "-- MIGRATIONS UPGRADE -START- --"
echo "------------------------"
python manage.py db upgrade
echo "------------------------"
echo "-- MIGRATIONS UPGRADE -END- --"
echo "------------------------"

python manage.py run
