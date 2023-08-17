QUASAR_URL=https://registry.npmjs.org/quasar/-/quasar-2.12.4.tgz
mkdir -p .download && cd .download && curl -L $QUASAR_URL | tar --strip-components=1 -xzv
cd ..
python ./.generator/generate.py
python -m trame.tools.widgets --config ./.generator/config.yaml --output ./