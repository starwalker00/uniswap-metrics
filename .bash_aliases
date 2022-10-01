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

function run_uniswapy {
  python3 main_uniswapy.py
}

function run_alchemy {
  python3 main_alchemy.py
}
