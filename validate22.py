import os
import sys
import argparse
from lxml import etree

def validate_xliff_22(xliff_file_path):
    # 1. Setup paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    schema_dir = os.path.join(base_dir, "Core")
    master_schema_path = os.path.join(schema_dir, "xliff_core_2.2.xsd")

    if not os.path.exists(master_schema_path):
        print(f"Error: Master schema not found at {master_schema_path}")
        return

    try:
        # 2. Load schema (temporarily switching CWD to resolve relative includes)
        original_cwd = os.getcwd()
        os.chdir(schema_dir)
        
        with open("xliff_core_2.2.xsd", 'rb') as f:
            schema_root = etree.XML(f.read())
            schema = etree.XMLSchema(schema_root)

        # 3. Validate target file
        os.chdir(original_cwd)
        if not os.path.exists(xliff_file_path):
            print(f"Error: File '{xliff_file_path}' not found.")
            return

        with open(xliff_file_path, 'rb') as f:
            xliff_doc = etree.parse(f)

        if schema.validate(xliff_doc):
            print(f"✅ Success: '{xliff_file_path}' is a valid XLIFF 2.2 file.")
        else:
            print(f"❌ Validation Failed for '{xliff_file_path}':")
            for error in schema.error_log:
                print(f"  - Line {error.line}: {error.message}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        os.chdir(original_cwd)

if __name__ == "__main__":
    # Setup the command-line argument parser
    parser = argparse.ArgumentParser(description="Validate an XLIFF 2.2 file against OASIS schemas.")
    parser.add_argument("file", help="Path to the .xlf or .xliff file to validate")
    
    args = parser.parse_args()
    validate_xliff_22(args.file)
