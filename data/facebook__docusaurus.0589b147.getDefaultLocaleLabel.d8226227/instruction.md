# Bug Report

### Describe the bug

When using the default locale configuration, the locale label is not being generated correctly. The first character appears to be capitalized, but the rest of the language name is missing - only the first character is shown.

### Reproduction

```js
// When getting the default locale label
const label = getDefaultLocaleLabel('en');
// Expected: "English"
// Actual: "E"
```

This affects any locale where the default label needs to be generated from the language name. The label ends up being just a single uppercase character instead of the full capitalized language name.

### Expected behavior

The default locale label should display the full language name with the first letter capitalized (e.g., "English" for 'en', "Français" for 'fr', etc.).

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
