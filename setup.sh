# install react and other required npm packages
cd frontend && npm install
echo -e "\e[32m>>>> Node dependencies installed successfully with npm.\e[0m"

# create python3 virtualenv
cd ../backend && python3 -m venv venv && source venv/bin/activate
echo -e "\e[32m>>>> Python3 virtualenv created successfully.\e[0m"

# install required packages with pip3
pip3 install -r requirements.txt
echo -e "\e[32m>>>> Python requirements installed successfully with Pip.\e[0m"

# generate SECRET_KEY
cd backend/ && python3 keygen.py

echo -e "\e[32m>>>> Django SECRET_KEY generated successfully.\e[0m"

cd ../../ && echo "secrets.py" >> .gitignore

echo -e "\e[32m>>>> Django SECRET_KEY added to git-ignored files.\e[0m"

# setup django app:
cd backend && python3 manage.py makemigrations && python3 manage.py migrate
echo -e "\e[32m>>>> Database constructed, migrations applied.\e[0m"

# optionally fill database with sample data:
echo -e "\e[34m>>>> Do you want to fill database with sample data?\e[0m"
echo ""
echo -e "\e[34m>>>> Type 1 or 2 and hit ENTER.\e[0m"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) python3 manage.py loaddata data.json && echo -e "\e[32m >>>> Database filled with sample data.\e[0m"; break;;
        No ) echo -e "\e[36m>>>> Filling database with fixtures skipped.\e[0m"; break;;
    esac
done

echo -e "\e[32m>>>> Setup done.\e[0m"
