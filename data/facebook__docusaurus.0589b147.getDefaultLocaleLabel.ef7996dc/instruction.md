# Bug Report

### Describe the bug

When using i18n with certain locales, the default locale label is not being generated correctly. The first character appears to be capitalized, but the rest of the locale name is missing or replaced with just the first character repeated.

### Reproduction

```js
// When getting the default locale label for a language
const label = getDefaultLocaleLabel('french');

// Expected: "French"
// Actual: "F" (only the first character)
```

This affects the display of locale names in the language selector and other UI elements where locale labels are shown.

### Expected behavior

The locale label should be properly capitalized with the first letter uppercase and the remaining letters from the original language name preserved. For example:
- `'french'` should become `'French'`
- `'spanish'` should become `'Spanish'`
- `'german'` should become `'German'`

Instead, only the first character is being returned.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
