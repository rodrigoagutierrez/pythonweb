source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt 
rm -rf public
reflex init
reflex export --fontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate