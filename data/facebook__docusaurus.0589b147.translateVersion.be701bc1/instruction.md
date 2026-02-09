# Bug Report

### Describe the bug

I'm experiencing an issue with version label translations in the docs plugin. When I have a custom version label configured in my `versions.json`, the translation system seems to be overriding it incorrectly. The version label is not being used as expected when looking up translation files.

### Reproduction

```js
// versions.json
{
  "label": "2.0.0-beta",
  "versionName": "2.0.0"
}

// i18n translation file should be named based on version label
// But it seems to be using versionName instead
```

Steps to reproduce:
1. Set up a docs version with a custom label that differs from versionName
2. Add translation files for that version
3. The translation lookup fails because it's using the wrong property to determine the file name

### Expected behavior

The translation file lookup should use the version label (not versionName) to find the correct translation file. Additionally, when a custom label is already set in the version config, it should take precedence over the translated label from the translation files.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
