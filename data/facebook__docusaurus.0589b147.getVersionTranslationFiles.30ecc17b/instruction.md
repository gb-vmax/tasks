# Bug Report

### Describe the bug

Version labels are not appearing in the translation files for docs. After updating, I noticed that the version label translations are completely missing from the generated translation JSON files.

### Reproduction

1. Set up a Docusaurus site with versioned docs
2. Configure a custom version label in `versions.json` or `versioned_sidebars/version-X.X-sidebars.json`
3. Run the translation extraction
4. Check the generated translation files

Expected translation file content:
```json
{
  "version.label": {
    "message": "1.0.0",
    "description": "The label for version 1.0.0"
  },
  ...
}
```

Actual translation file content:
```json
{
  // version.label is missing entirely
  ...
}
```

### Expected behavior

The version label should be included in the translation files so it can be localized. The `version.label` key should appear in the generated translation JSON with the appropriate message and description.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
