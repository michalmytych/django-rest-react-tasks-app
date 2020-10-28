#!/bin/bash

error_count=0

# install react and other required npm packages
cd frontend && npm install

if [ $? -eq 0 ]; then
   echo -e "\e[32m>>>> Node dependencies installed successfully with npm.\e[0m"
else
   echo -e "\e[31m>>>> Error while installing Node dependencies.\e[0m"
   error_count += 1
fi

# create python3 virtualenv
cd ../backend && python3 -m venv venv && source venv/bin/activate

if [ $? -eq 0 ]; then
   echo -e "\e[32m>>>> Python3 virtualenv created successfully.\e[0m"
else
   echo -e "\e[31m>>>> Error while creating Python3 virtualenv.\e[0m"
   error_count += 1
fi

# install required packages with pip3
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
   echo -e "\e[32m>>>> Python requirements installed successfully with Pip.\e[0m"
else
   echo -e "\e[31m>>>> Error while installing requirements from requirements.txt\e[0m"
   error_count += 1
fi

# generate SECRET_KEY
cd backend/ && python3 keygen.py

if [ $? -eq 0 ]; then
   echo -e "\e[32m>>>> Django SECRET_KEY generated successfully.\e[0m"
else
   echo -e "\e[31m>>>> Error while generating Django SECRET_KEY\e[0m"
   error_count += 1
fi

cd ../../ && echo "secrets.py" >> .gitignore


if [ $? -eq 0 ]; then
   echo -e "\e[32m>>>> Django SECRET_KEY added to git-ignored files.\e[0m"
else
   echo -e "\e[31m>>>> Error while adding SECRET_KEY to git-ignored files.\e[0m"
   error_count += 1
fi

# setup django app:
cd backend && python3 manage.py makemigrations && python3 manage.py migrate

if [ $? -eq 0 ]; then
   echo -e "\e[32m>>>> Database constructed, migrations applied.\e[0m"
else
   echo -e "\e[31m>>>> Error while constructing database.\e[0m"
   error_count += 1
fi

# optionally fill database with sample data:
echo -e "\e[34m>>>> Do you want to fill database with sample data?\e[0m"
echo ""
echo -e "\e[34m>>>> Type 1 or 2 and hit ENTER.\e[0m"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) python3 manage.py loaddata data.json; break;;
        No ) echo -e "\e[36m>>>> Filling database with fixtures skipped.\e[0m"; break;;
    esac
done

if [ $? -eq 0 ]; then
    echo -e "\e[32m >>>> Database filled with sample data.\e[0m"
else
    echo -e "\e[31m>>>> Error while filling database with sample data.\e[0m"
    error_count += 1
fi

if [ $error_count -eq 0 ]; then
   echo -e "\e[32m>>>> *** Setup done. ***\e[0m"
else
   echo -e "\e[31m>>>> Setup failed. $error_count errors occured.\e[0m"
fi
