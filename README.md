#### Installation guide

Emenu app. Tested on python3.4, python3.5, nodeJS v6.9.4.

Install instructions for linux/mac

+ Clone sources from github

```bash
git clone https://github.com/wmolicki/emenu.git
```

+ Install requirements

Start with creating virtualenv and installing python packages:

```bash
virtualenv --python=/usr/bin/python3 ~/venv/emenu-env/
source ~/venv/emenu-env/bin/activate
cd emenu
pip install --requirements=requirements.txt
```

+ Migrate database (sqlite3 by default) and create menu, dish and user fixtures.
```bash
python manage.py migrate
python manage.py create_fakes
```

Use local node or install new node version with nvm (https://github.com/creationix/nvm). To install node version v6.9.4 run:
```bash
nvm install 6.9.4 --version
nvm use 6.9.4
```

In case you have node, install dependencies with npm:

```bash
cd menu/www
npm install
npm install -g webpack
```

+ Run webpack to compile static files:
```bash
webpack --watch
```

+ Run tests with pytest (show coverage results by opening `htmlcov/index.html` in web browser)

```bash
pytest
```


+ Run django's dev server to serve ng-api. We also serve static files from there.

```bash
python manage.py runserver 0.0.0.0:8001
```


+ Open app on [http://0.0.0.0:8001](http://0.0.0.0:8001). You can access django-admin 
using credentials: _admin@password123_ at [http://0.0.0.0:8001/admin/](http://0.0.0.0:8001/admin/). 


