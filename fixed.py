import json

notebook_path = "DL_Clinical_EWS_FINAL.ipynb"
fixed_path = "Fixed_DL_Clinical_EWS_FINAL_106.ipynb"

# 1. Open and load your raw notebook structure
with open(notebook_path, "r", encoding="utf-8") as f:
    notebook_data = json.load(f)

# 2. Check if the top-level 'metadata' dictionary has the broken 'widgets' key
if "widgets" in notebook_data.get("metadata", {}):
    del notebook_data["metadata"]["widgets"]
    print("Success: Removed corrupted 'metadata.widgets' entry.")
else:
    print("No isolated 'widgets' key found in the top-level notebook metadata.")

# 3. Write it back out to a pristine file
with open(fixed_path, "w", encoding="utf-8") as f:
    json.dump(notebook_data, f, indent=1)

print(f"Cleaned notebook saved to: {fixed_path}")