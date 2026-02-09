# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin where version translation files are being generated with incorrect filenames and content. The `version.label` message is using `version.versionName` instead of the actual label, and the translation file path is using `version.label` instead of `version.versionName`.

### Reproduction

```js
// When a version has different label and versionName
const version = {
  versionName: '1.0.0',
  label: 'Version 1.0'
}

// The translation file is generated with:
// - filename based on label: getVersionFileName('Version 1.0')
// - but message content uses versionName: message: '1.0.0'

// This causes a mismatch between the filename and the content
```

### Expected behavior

The translation file should be generated consistently:
- The filename should be based on `versionName` (e.g., `version-1.0.0.json`)
- The `version.label` message should contain the actual `label` value (e.g., `'Version 1.0'`)

This way the translation files are properly named and contain the correct translatable strings.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
