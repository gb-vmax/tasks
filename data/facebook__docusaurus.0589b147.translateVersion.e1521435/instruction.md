# Bug Report

### Describe the bug

After a recent update, version labels are not displaying correctly in the documentation. The fallback behavior for version labels seems broken - when a translation is missing, the label doesn't fall back to the original version label as expected.

### Reproduction

1. Set up a docs version with a custom label (e.g., `label: "1.0.0"` in versions.json)
2. Don't provide a translation for `version.label` in the translation files
3. The version label appears as `undefined` instead of showing "1.0.0"

Also noticed that the translation file lookup might be using the wrong key - it seems to be looking for a file based on `version.label` instead of `version.versionName`, which could cause issues when the label differs from the version name.

### Expected behavior

When no translation is available, the version label should fall back to the original `version.label` value from the version configuration. The translation file should be looked up using the version name, not the label.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
