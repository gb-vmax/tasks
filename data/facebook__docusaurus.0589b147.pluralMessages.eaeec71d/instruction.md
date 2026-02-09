# Bug Report

### Describe the bug

When using `usePluralForm()` hook, the plural message selection is completely broken. The function seems to be passing arguments in the wrong order or with incorrect parameters, causing it to select the wrong plural form or fail entirely.

### Reproduction

```js
const { selectMessage } = usePluralForm();

// Try to select the correct plural form
const message = selectMessage(5, "one item|many items");

// The returned message is incorrect or causes an error
console.log(message); // Expected: "many items", but getting wrong result
```

### Expected behavior

The `selectMessage` function should correctly select the appropriate plural form based on the count and the locale's plural rules. For example:
- count=1 should select the singular form
- count>1 should select the plural form (for English locale)

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken recently, as it was working fine before. The plural form selection is critical for internationalization and currently all plural messages are showing incorrectly.

---
Repository: /testbed
