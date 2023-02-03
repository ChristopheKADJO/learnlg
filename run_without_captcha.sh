cd src/accounts/
sed -i '4d;5d;25d;47d' forms.py

cd templates/accounts/
sed -i '44d;45d;46d;47d;82d;83d;84d' register.html
sed -i '34d;35d;36d;37d;58d;59d;60d' login.html

cd ../../../learnlg/
sed -i '3d;4d' .env
sed -i '43d;141d;142d;143d;144d' settings.py

echo "|"
echo "|"
echo "|"
echo "|"
echo "|"
echo "|"
echo "|"
echo "|"
echo "--------------------------------------"
echo "Recaptcha elements deletion completed!"
echo "--------------------------------------"