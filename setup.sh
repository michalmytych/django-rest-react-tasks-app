# install react and other required npm packages
cd frontend && npm install

# create python3 virtualenv
cd ../backend && python3 -m venv venv && source venv/bin/activate

# install required packages with pip3
pip3 install -r requirements.txt

# setup django app:
python3 manage.py makemigrations && python3 manage.py migrate

# optionally fill database with sample data:
echo "Do you want to fill database with sample data? Type 1 or 2 and hit ENTER."
select yn in "Yes" "No"; do
    case $yn in
        Yes ) python3 manage.py loaddata data.json; break;;
        No ) exit;;
    esac
done
