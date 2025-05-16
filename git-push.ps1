# Git Auto Commit + Pull --rebase + Push Script

param (
    [string]$message = "Güncelleme yapıldı"
)

Write-Host "Degisiklikler ekleniyor..." -ForegroundColor Cyan
git add .

Write-Host "Commit islemi yapiliyor: '$message'" -ForegroundColor Yellow
git commit -m "$message"

Write-Host "Uzaktan degisiklikler cekiliyor (rebase)..." -ForegroundColor Green
git pull origin main --rebase

Write-Host "Degisiklikler push ediliyor..." -ForegroundColor Magenta
git push origin main

Write-Host "Tum islemler tamamlandi!" -ForegroundColor Cyan

Set-Alias gpush C:\Users\ensko\vscodeProjects\python\Fundamentals\git-push.ps1
# Usage: gpush "Your commit message"