# XLIFF 2.2 Validator

A Python-based validator for XLIFF 2.2 files using local OASIS schema files.

## Features

- ✅ Validates XLIFF 2.2 files against official OASIS schemas
- ✅ Uses local schema files (no internet connection required)
- ✅ Detailed error reporting with line numbers and descriptions
- ✅ Smart schema file detection (supports multiple schema filenames)
- ✅ Simple command-line interface
- ✅ Proper handling of schema includes and imports

## Requirements

- Python 3.6 or higher
- lxml library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/piotr-bienkowski/Xliff2-validator.git
cd xliff-validator
```

2. Install dependencies:
```bash
pip install lxml
```

3. Ensure schema files are present in the `Core/` directory (see Schema Files section below)

## Usage

### Basic Usage

```bash
python validate22.py your_file.xlf
```

### Examples

Validate a single XLIFF file:
```bash
python validate22.py translation.xlf
```

Expected output for valid file:
```
✓ translation.xlf is valid XLIFF 2.2
```

Expected output for invalid file:
```
✗ translation.xlf has validation errors:
Line 15: Element '{urn:oasis:names:tc:xliff:document:2.0}target': This element is not expected.
```

## Schema Files

This validator requires XLIFF 2.2 schema files in the `Core/` directory.

### Option 1: Download from OASIS (Recommended)

Download the official schemas from:
https://docs.oasis-open.org/xliff/xliff-core/v2.2/os/schemas/

Required files:
- `xliff_core_2.2.xsd` (and `xliff_core_2.0.xsd`)
- Supporting schema files (imports and includes)

Place all files in the `Core/` directory.

### Option 2: Use Included Schemas

If schema files are already included in this repository, no additional setup is needed.

**Schema Copyright Notice:**
The XLIFF 2.2 schema files are copyright © OASIS Open. All Rights Reserved.
These schemas are used under the terms specified by OASIS.
Source: https://www.oasis-open.org/committees/xliff/

## How It Works

1. The validator reads your XLIFF file
2. Loads the XLIFF 2.2 schema from the `Core/` directory
3. Temporarily changes working directory to resolve schema includes/imports
4. Validates the XLIFF structure against the schema
5. Reports any validation errors with line numbers

## Project Structure

```
xliff-validator/
├── README.md              # This file
├── validate22.py          # Main validator script
├── Core/                  # XLIFF 2.2 schema files
│   ├── xliff_core_2.2.xsd
│   └── (other schema files)
└── .gitignore            # Git ignore patterns
```

## Common Use Cases

### Validating Converted Files

If you've converted SDLXLIFF files to XLIFF 2.2, use this validator to ensure the output is schema-compliant:

```bash
python validate22.py converted_output.xlf
```

### Batch Validation

Validate multiple files using a shell loop:

```bash
for file in *.xlf; do
    python validate22.py "$file"
done
```

### Integration with Translation Tools

Use this validator in your translation workflow to ensure files are valid before processing:

```bash
# Convert file
python sdlxliff_to_xliff22.py input.sdlxliff -o output.xlf

# Validate output
python validate22.py output.xlf
```

## Troubleshooting

### "Schema file not found"
- Ensure the `Core/` directory exists
- Check that schema files are present
- Verify the schema filename matches supported names

### "Failed to load schema"
- Check that all imported schema files are present
- Ensure proper file permissions
- Verify schema files are not corrupted

### "Element not expected" errors
- Your XLIFF file may not be valid XLIFF 2.2
- Check the XLIFF version in the root element
- Ensure proper namespace usage

## Technical Details

### Supported Schema Filenames

The validator automatically detects these schema filenames:
- `xliff_core_2.2.xsd`
- `xliff_core_2.0.xsd` (XLIFF 2.2 uses 2.0 namespace)
- `xliff-core-2.2.xsd`

### Namespace

XLIFF 2.2 uses the namespace:
```
urn:oasis:names:tc:xliff:document:2.0
```

Note: XLIFF 2.2 uses the 2.0 namespace for backward compatibility.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Test your changes
5. Commit (`git commit -am 'Add new feature'`)
6. Push to branch (`git push origin feature/improvement`)
7. Open a Pull Request

## Related Projects

- **SDLXLIFF to XLIFF 2.2 Converter** - Convert SDL Trados SDLXLIFF files to XLIFF 2.2
- **Converter** mentioned above will be coming soon

## License

This utility is made available under the MIT license.

## Author

piotr-bienkowski

## Acknowledgments

- OASIS XLIFF Technical Committee for the XLIFF standard
- lxml library developers

## Resources

- [XLIFF 2.2 Specification](https://docs.oasis-open.org/xliff/xliff-core/v2.2/)
- [OASIS XLIFF TC](https://www.oasis-open.org/committees/xliff/)
- [lxml Documentation](https://lxml.de/)

## Version History

### 1.0.0 (Current)
- Initial release
- Support for XLIFF 2.2 validation
- Local schema file support
- Detailed error reporting
