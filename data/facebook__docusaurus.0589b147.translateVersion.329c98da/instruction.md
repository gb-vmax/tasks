# Bug Report

### Describe the bug

When using versioned docs, the version label translations are not being applied correctly. The translation file lookup is using the wrong key, which causes translations to fail silently and fall back to the default version label.

### Reproduction

1. Set up a Docusaurus site with versioned docs
2. Create a version with a custom `versionName` that differs from the `label`
3. Add translations for the version label in your translation files
4. Build or serve the site

Expected: The translated version label should be displayed
Actual: The default version label is shown instead, translations are ignored

Example version config:
```js
{
  versionName: '1.0',
  label: 'Version 1.0.0'
}
```

The translation file would be keyed by the version name, but the code is looking it up using the label instead, causing a mismatch.

### Expected behavior

Version label translations should be properly loaded and applied when the translation files are keyed by `versionName`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
