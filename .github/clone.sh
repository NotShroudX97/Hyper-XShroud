#!/bin/bash

# Copyright (C) 2020 by sandy1709

echo "
hey master
HYPER-X BOT ZINDA THA HAI AUR RHEGA
"

FILE=/app/.git

if [ -d "$FILE" ] ; then
    echo "$FILE directory exists already."
else
    rm -rf userbot
    rm -rf .github
    rm -rf requirements.txt
    git clone https://github.com/sameerpanthi/HYPER-X  HYPER-X_ub
    mv next-level_ub/userbot .
    mv next-level_ub/.github . 
    mv next-level_ub/.git .
    mv next-level_ub/requirements.txt .
    rm -rf cat_ub
    python ./.github/update.py
fi

FILE=/app/bin/
if [ -d "$FILE" ] ; then
    echo "$FILE directory exists already."
else
    bash ./.github/bins.sh
fi

python -m userbot
