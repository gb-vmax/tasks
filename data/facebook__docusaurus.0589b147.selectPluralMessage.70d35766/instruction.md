# Bug Report

### Describe the bug

I'm experiencing an issue with plural form selection in the translation system. When using plural messages with multiple forms separated by `|`, the wrong plural form is being selected for certain counts.

### Reproduction

```js
// Example with a language that has multiple plural forms
// For example, Russian or Polish where different numbers use different forms

// Given a plural message like: "1 item|{count} items|{count} many items"
// When count = 5, it should select the third form
// But instead, it always seems to select the last form regardless of the count

const message = "1 предмет|{count} предмета|{count} предметов";
// With count = 2, expected: "{count} предмета" (few)
// Actual: "{count} предметов" (many)
```

### Expected behavior

The plural form selector should correctly map the count to the appropriate plural form based on the locale's plural rules. For languages with multiple plural forms (like Slavic languages), different counts should trigger different message variants.

For instance:
- count = 1 → first form
- count = 2-4 → second form  
- count = 5+ → third form

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
