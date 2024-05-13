QUASAR_URL=https://registry.npmjs.org/quasar/-/quasar-2.12.4.tgz
FONTS_URL="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900|Material+Icons"
mkdir -p .download && cd .download && curl -L $QUASAR_URL | tar --strip-components=1 -xzv
cd ..
python ./.generator/generate.py
curl -o ./.download/fonts_with_urls.css "$FONTS_URL"
python ./.generator/get_fonts.py

python -m trame.tools.widgets --config ./.generator/config.yaml --output ./
mv ./.generator/*.ttf ./trame_quasar/module/quasar/vue3/
