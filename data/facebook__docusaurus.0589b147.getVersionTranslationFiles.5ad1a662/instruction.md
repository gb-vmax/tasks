# Bug Report

### Describe the bug

The version label and version name appear to be swapped in the translation files. When looking at the generated translation files, the `version.label` message contains the version name instead of the actual label, and the description references the label instead of the version name.

### Reproduction

1. Set up a versioned docs plugin with custom version labels
2. Generate translation files for a version
3. Check the `version.label` translation entry

For example, if you have:
- Version name: `1.0.0`
- Version label: `Latest`

The translation file will show:
```json
{
  "version.label": {
    "message": "1.0.0",
    "description": "The label for version Latest"
  }
}
```

### Expected behavior

The `version.label` message should contain the actual label (`Latest`), not the version name (`1.0.0`). The description should reference the version name, not the label.

Expected output:
```json
{
  "version.label": {
    "message": "Latest",
    "description": "The label for version 1.0.0"
  }
}
```

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
