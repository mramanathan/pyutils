#!/bin/bash

export PYENV_ROOT=$HOME/.pyenv
export PATH=${PYENV_ROOT}/bin:${PATH}

PYTHON_VERSION=2.7.12
VENV_DIR=flake8_temp

if [ ! -d "${PYENV_ROOT}" ]; then
  echo "~> Installing PyEnv..."
  curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
fi

if [ ! -d "$PYENV_ROOT/plugins/pyenv-virtualenv" ]; then
  echo "Installing pyenv-virtualenv ..."
  git clone https://github.com/yyuu/pyenv-virtualenv.git $PYENV_ROOT/plugins/pyenv-virtualenv
fi

curdir=pwd

# Update pyenv and pyenv-virtualenv
echo "~> Updating pyenv and pyenv-virtualenv"
pyenv update
pushd $PYENV_ROOT/plugins/pyenv-virtualenv
git pull
popd

echo "~> Initializing pyenv..."
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
export PYENV_VIRTUALENV_DISABLE_PROMPT=1 

echo "~> Activating pyenv virtualenv..."
pyenv virtualenv "${PYTHON_VERSION}" "${VENV_DIR}"

echo "~> Installing flake8 packages..."
cat << PKGS > requirements.txt
    flake8
    flake8-builtins
    flake8-pep257
    flake8-mock
    flake8-coding
    flake8-print
    flake8-future-import
    flake8-import-order
    flake8-builtins
    flake8-commons
    pepper8
    pep8-naming
PKGS


echo "~> Installing Python packages..."
pip install -r requirements.txt


echo "~> PyEnv Versions"
pyenv versions
echo "~> Current Versions:"
echo -ne "~> pyenv version: " && pyenv version
python --version
pip --version
echo "~> Virtual Envs:"
pyenv virtualenvs
echo "~> Installed Python packages:"
pip freeze

echo "~> Fetching sources to run flake8..."
git clone https://github.com/mramanathan/pyutils.git
cd pyutils
flake8 --statistics -q pyutils/*