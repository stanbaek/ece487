# ece487
ECE487 Machine Learning Course Web

### How to install required Python packages? 
- Open a terminal.
- Navigate to the root folder and find requirements.txt
- run `pip install -r requirements.txt`
- I recommned using a virtual environment.

### How to build and publish?
- Run the following under the `docs` folder.
- Build: `jupyter-book build --all .`  
- Publish: `ghp-import -n -p -f _build/html` 

### Recommended extensions for vscode
- Python, Python Extension Pack
- Jupyter, MyST-Markdown

### Convert Jupyter notebooks to markdown files
- jupytext notebook.ipynb --to md


### To remove version constraints

To remove version constraints from a requirements.txt file (e.g., turning numpy==1.23.4 into numpy), you can use a simple shell command or Python script.
```bash
sed -E 's/[<=>~!]=?.*//' requirements.txt > requirements_no_versions.txt
```
