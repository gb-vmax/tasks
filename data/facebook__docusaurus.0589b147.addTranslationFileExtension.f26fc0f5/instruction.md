# Bug Report

### Describe the bug

Translation files are being generated with incorrect file paths. The `.json` extension is appearing at the beginning of the file path instead of at the end, resulting in files like `.json/i18n/en/code.json` instead of `/i18n/en/code.json`.

### Reproduction

When running the translation generation:

1. Configure a Docusaurus site with i18n enabled
2. Run the command to write translations
3. Check the generated translation file paths

Expected file path: `i18n/en/docusaurus-plugin-content-docs/current.json`
Actual file path: `.jsoni18n/en/docusaurus-plugin-content-docs/current`

### Expected behavior

Translation files should be created with the `.json` extension appended to the end of the file path, not prepended to the beginning. The validation should also check if the path ends with `.json`, not if it starts with `.json`.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
