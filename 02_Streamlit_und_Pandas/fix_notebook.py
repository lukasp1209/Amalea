import json

notebook_path = '/Users/kqc/amalea/02_Streamlit_und_Pandas/01_Erste_Streamlit_App_fixed.ipynb'

def fix_notebook(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    fixed = False
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            if len(source) >= 2:
                # Check if the first line is a comment and second is %%writefile
                if source[0].strip().startswith('#') and source[1].strip().startswith('%%writefile'):
                    # Swap the first two lines
                    source[0], source[1] = source[1], source[0]
                    cell['source'] = source
                    fixed = True
                    print(f"Fixed cell starting with: {source[0].strip()}")

    if fixed:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1)
        print(f"Successfully fixed {path}")
    else:
        print(f"No issues found in {path}")

if __name__ == '__main__':
    fix_notebook(notebook_path)