import nbformat

# Load your notebook
nb_path = "notebooks/transformer_main_finetuning.ipynb"
with open(nb_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

# Remove problematic widget metadata
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# Save back (keeps all outputs intact)
with open(nb_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Cleaned notebook — outputs preserved!")