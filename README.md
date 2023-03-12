# Pylint plugin for GitHub Actions annotations
This is a plugin for [Pylint](https://www.pylint.org/) that allows it to output annotations 
in the format that GitHub Actions understands. 
See annotations from [examples](https://github.com/skhomuti/pylint-actions/actions/workflows/example.yml) workflows.
Also these annotations will be displayed in your pull requests changes

# Installation
So simple:
```bash
pip install pylint-actions
```

# Usage
Add the following to your `pyproject.toml` file:
```toml
[tool.pylint.main]
load-plugins = "pylint_actions"
```
Or load the plugin with any available pylint configuration variants except command line arguments.

Next, run pylint with the `--output-format=actions` option, or shorted `-f actions`.

In your GitHub Actions workflow, use it like this:
```yaml
- name: Run pylint
  run: poetry run pylint -f actions src
```