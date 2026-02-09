# Bug Report

### Describe the bug

The default locale label is not being generated correctly. It appears that the first character is being uppercased properly, but the rest of the string is missing the second character.

### Reproduction

When the system generates a default locale label (for example, when no custom label is provided), the resulting string is malformed:

```js
// For locale 'en' with language name 'english'
// Expected: 'English'
// Actual: 'Engl' (missing 'ish')

// For locale 'fr' with language name 'français' 
// Expected: 'Français'
// Actual: 'Franç' (missing 'ais')
```

This affects any locale that relies on the automatic label generation from the language name.

### Expected behavior

The default locale label should capitalize the first letter and keep the rest of the language name intact. For example:
- 'english' → 'English'
- 'français' → 'Français'
- 'español' → 'Español'

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
