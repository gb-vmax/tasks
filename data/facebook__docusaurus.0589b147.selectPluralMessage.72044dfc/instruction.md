# Bug Report

### Describe the bug

I'm experiencing an issue with plural form message selection in the theme. When using the plural form utility with messages separated by `|`, the wrong message variant is being returned for certain count values.

### Reproduction

```js
// Example with locale that has multiple plural forms
const messages = "1 item|{count} items";
const count = 5;

// Expected: "{count} items" (plural form)
// Actual: Returns wrong variant or incorrect message
```

The issue seems to affect languages with multiple plural forms. The selection logic appears to be choosing the incorrect message variant based on the count value.

### Expected behavior

The function should correctly select the appropriate plural form message based on the count and locale plural rules. For example:
- count = 1 should return "1 item"
- count = 5 should return "{count} items"

### Additional context

This affects the display of pluralized strings throughout the theme (e.g., "X items", "Y results", etc.). The messages are getting mixed up or showing the wrong variant for the given count.

---
Repository: /testbed
