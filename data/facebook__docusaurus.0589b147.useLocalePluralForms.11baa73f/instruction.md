# Bug Report

### Describe the bug

When switching between locales in a Docusaurus site, the plural forms are not updating correctly. The pluralization continues to use the initial locale's rules even after the locale has been changed.

### Reproduction

```js
// Initial locale: 'en'
const pluralForm = usePluralForm();
pluralForm.selectMessage(1, ['1 item', 'multiple items']); // Works correctly

// Switch locale to 'fr' or another language
// Try to use plural forms again
pluralForm.selectMessage(1, ['1 élément', 'plusieurs éléments']); 
// Still uses English plural rules instead of French rules
```

### Steps to reproduce:
1. Start with a default locale (e.g., English)
2. Use the locale switcher to change to a different language
3. Navigate to a page that uses plural forms
4. The plural forms still follow the initial locale's pluralization rules

### Expected behavior

The plural forms should update dynamically when the locale changes. Each locale has different pluralization rules (e.g., English has 2 forms, Polish has 4 forms), and these should be applied correctly based on the currently active locale.

### System Info
- Docusaurus version: latest
- Browser: Any

---
Repository: /testbed
