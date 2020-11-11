#!/bin/bash

ERROR_COUNT=0

# Sets up colors of text
setup_color() {
	if [ -t 1 ]; then
		RED=$(printf '\033[31m')
		GREEN=$(printf '\033[32m')
		YELLOW=$(printf '\033[33m')
		BLUE=$(printf '\033[34m')
		RESET=$(printf '\033[m')
	else
		RED=""
		GREEN=""
		YELLOW=""
		BLUE=""
		RESET=""
	fi
}

# Error handler, $1 is success message, $2 is error message
handle_errors() {
   if [ $? -eq 0 ]; then
      echo -e $1
   else
      echo -e $2
      ERROR_COUNT+=1
   fi
}

display_start_message() {
   echo -e "$BLUE>>>> Starting app setup... <<<<$RESET"
}

setup_frontend () {
   cd frontend && npm install

   handle_errors "$GREEN>>>> Node dependencies installed successfully with npm. <<<<$GREEN" "$RED>>>> Error while installing Node dependencies. <<<<$RESET"
}

setup_python_venv() {
   cd ../backend && python3 -m venv venv && source venv/bin/activate

   handle_errors "$GREEN>>>> Python3 virtualenv created successfully. <<<<$RESET" "$RED>>>> Error while creating Python3 virtualenv. <<<<$RESET"
}

install_requirements() {
   pip3 install -r requirements.txt

   handle_errors "$GREEN>>>> Python requirements installed successfully with Pip. <<<<$RESET" "$RED>>>> Error while installing requirements from requirements.txt <<<<$RESET"
}

generate_django_secret_key() {
   cd backend/ && python3 keygen.py

   handle_errors "$GREEN>>>> Django SECRET_KEY generated successfully. <<<<$RESET" "$RED>>>> Error while generating Django SECRET_KEY <<<<$RESET"

   cd ../../ && echo "secrets.py" >> .gitignore
   
   handle_errors "$GREEN>>>> Django SECRET_KEY added to git-ignored files. <<<<$RESET" "$RED>>>> Error while adding SECRET_KEY to git-ignored files. <<<<$RESET"
}

setup_database() {
   cd backend && python3 manage.py makemigrations && python3 manage.py migrate

   handle_errors "$GREEN>>>> Database constructed, migrations applied. <<<<$RESET" "$RED>>>> Error while constructing database. <<<<$RESET"
}

load_fixtures() {
   python3 manage.py loaddata data.json

   handle_errors "$GREEN >>>> Database filled with sample data. <<<<$RESET" "$RED>>>> Error while filling database with sample data. <<<<$RESET"
}

fill_database_if_wanted() {
   echo -e "$BLUE>>>> Do you want to fill database with sample data? <<<<$RESET"
   echo ""
   echo -e "$BLUE>>>> Type 1 or 2 and hit ENTER. <<<<$RESET"
   select yn in "Yes" "No"; do
      case $yn in
         Yes ) load_fixtures; break;;
         No ) echo -e "$YELLOW>>>> Filling database with fixtures skipped. <<<<$RESET"; break;;
      esac
   done
}

check_if_setup_succedeed() {
   if [ $ERROR_COUNT -eq 0 ]; then
      echo -e "$GREEN>>>> *** Setup done. *** <<<< $RESET"
   else
      echo -e "$RED>>>> Setup failed. $ERROR_COUNT errors occured. <<<<$RESET"
   fi
}

create_superuser_if_wanted() {
   echo -e "$BLUE>>>> Do you want to create superuser (admin user) now? <<<<$RESET"
   echo ""
   echo -e "$BLUE>>>> Type 1 or 2 and hit ENTER. <<<<$RESET"
   select yn in "Yes" "No"; do
      case $yn in
         Yes ) python3 manage.py createsuperuser; break;;
         No ) echo -e "$YELLOW>>>> Creating superuser skipped. <<<<$RESET"; break;;
      esac
   done
}

run_django_app() {
   echo -e "$BLUE>>>> Launching Django backend app... <<<<$RESET"

   cd ..
   source backend/venv/bin/activate && python3 backend/manage.py runserver

   handle_errors "$GREEN $BOLD >>>> Thanks for trying out this app :) <<<< $RESET" "$RED>>>> Error while running backend Django app. <<<<$RESET"
}

run_app_if_wanted() {
   echo -e "$BLUE>>>> Do you want to run Django API on port 8000 now? <<<<$RESET"
   echo ""
   echo -e "$BLUE>>>> Type 1 or 2 and hit ENTER. <<<<$RESET"
   select yn in "Yes" "No"; do
      case $yn in
         Yes ) run_django_app; break;;
         No ) echo -e "$YELLOW>>>> Running Django API skipped. <<<<$RESET"; break;;
      esac
   done
}

setup_app() {
   setup_color
   display_start_message
   setup_frontend
   setup_python_venv
   install_requirements
   generate_django_secret_key
   setup_database
   fill_database_if_wanted
   create_superuser_if_wanted
   check_if_setup_succedeed
}

setup_app

run_app_if_wanted
