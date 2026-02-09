# Bug Report

### Describe the bug

When using the `usePluralForm` hook to display pluralized messages, negative counts are being passed to the plural form selector instead of the actual count value. This causes incorrect plural forms to be selected for all message counts.

### Reproduction

```js
const { selectMessage } = usePluralForm();

// With count = 5, expecting plural form for 5 items
const message = selectMessage(5, '1 item|{count} items');
// Returns incorrect plural form because -5 is used internally
```

### Expected behavior

The `selectMessage` function should use the provided count value directly when selecting the appropriate plural form. For example:
- `selectMessage(1, '1 item|{count} items')` should return "1 item"
- `selectMessage(5, '1 item|{count} items')` should return "5 items"

Instead, the count is being negated before being passed to the plural form selector, which results in incorrect plural forms being selected.

### System Info
- Docusaurus version: latest
- Package: @docusaurus/theme-common

---
Repository: /testbed
