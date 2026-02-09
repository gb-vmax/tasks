# Bug Report

### Describe the bug

The `usePluralForm` hook is not working correctly - it's completely ignoring the `pluralMessages` parameter that's passed to `selectMessage`. This means that regardless of what plural message strings you provide, they won't be used at all.

### Reproduction

```js
const { selectMessage } = usePluralForm();

// Define plural messages for different counts
const messages = "1 item|{count} items";

// Try to get the correct plural form
const result = selectMessage(5, messages);

// Expected: "5 items"
// Actual: The messages parameter is ignored entirely
```

### Expected behavior

The `selectMessage` function should use the `pluralMessages` parameter to determine which message variant to display based on the count. Currently it seems like this parameter is just being discarded.

### System Info
- Docusaurus theme-common package

This is breaking pluralization in our documentation site. Any text that needs to change based on count (like "1 result" vs "5 results") is not working as expected.

---
Repository: /testbed
