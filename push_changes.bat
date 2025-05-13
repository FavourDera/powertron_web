@echo off
echo Pushing changes to GitHub...
git add .
git commit -m "Add Render deployment configuration and update requirements"
git push origin main
echo Done!
pause 