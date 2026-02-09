# Bug Report

### Describe the bug

When loading translation files, I'm seeing error messages logged even when the translation files are valid and load successfully. The error `Invalid translation file at path=...` appears in the console for every translation file that exists, regardless of whether the file content is actually valid or not.

### Reproduction

1. Create a valid translation JSON file (e.g., `i18n/en/code.json`)
2. Add proper translation content:
```json
{
  "theme.common.skipToMainContent": {
    "message": "Skip to main content"
  }
}
```
3. Start the Docusaurus dev server or build
4. Observe error messages in the console for valid translation files

### Expected behavior

Error messages should only be logged when translation files are actually invalid or malformed. Valid translation files should load silently without any error output.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is making it difficult to debug actual translation issues since the logs are flooded with false error messages.

---
Repository: /testbed
