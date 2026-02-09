# Bug Report

### Describe the bug

I'm encountering a syntax error when importing Swagger 2.0 specifications. The importer appears to be broken and fails to parse the spec file.

### Reproduction

Try importing any Swagger 2.0 specification file:

1. Open Insomnia
2. Go to Import/Export
3. Select a Swagger 2.0 spec file (JSON or YAML)
4. Click Import

The import process fails immediately with what looks like a parsing error.

### Expected behavior

The Swagger 2.0 spec should import successfully and generate the appropriate requests with parameters, just like it did in previous versions.

### Additional context

This seems to have started happening recently. I was able to import the same spec file without issues before. The spec file itself is valid and works fine with other tools.

---
Repository: /testbed
