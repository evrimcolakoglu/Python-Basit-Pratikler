@echo off
echo "Git'e guncellemeler ekleniyor..."
git add .
git commit -m "Otomatik guncelleme"
git push
echo "Islem tamamlandi."
pause
