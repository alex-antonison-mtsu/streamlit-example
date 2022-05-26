# Streamlit Database Example App

To get started with this, you will need to install Python 3.10. I recommend using pyenv, [see here for instructions](https://github.com/mtsu-data-science/data-science-sandbox/blob/main/environment-setup/setup-pyenv.md).

With Python 3.10 installed, you then need to install poetry to set up the virtual environment.

```bash
pip install poetry
```

With poetry installed, open your command line in this folder and run

```bash
poetry install
```

You then need to create a copy of the [.streamlit/secrets-sample.toml](.streamlit/secrets-sample.toml) to `.streamlit/secrets.toml` and then fill in the username, password, and host.

Once done, you can then do `make run-app` to run the streamlit app.
