#!/usr/bin/env bash

LANG="ja_JP.UTF-8"
PYENV_ROOT="${HOME}/.pyenv"
PATH="${PYENV_ROOT}/bin:${PATH}:/usr/local/bin"
eval "$(pyenv init -)"

DIR=$(dirname $1)
SCRIPT=$(basename $1)

cd ${DIR}
python ${SCRIPT}
