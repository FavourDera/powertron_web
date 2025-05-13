Write-Host "Pushing changes to GitHub..." -ForegroundColor Green
git add .
git commit -m "Add Render deployment configuration and update requirements"
git push origin main
Write-Host "Done!" -ForegroundColor Green
Read-Host "Press Enter to continue" 