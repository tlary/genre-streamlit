mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"tobias-larysch@gmx.net\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
