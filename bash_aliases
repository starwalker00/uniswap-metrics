function venv_create {
  python3 -m venv env
}

function venv_activate {
  source env/bin/activate
}

function venv_deactivate {
  deactivate
}

function pip_install {
  pip install -r requirements.txt
}

function pip_list {
  pip freeze
}

function run {
  python3 main.py
}
