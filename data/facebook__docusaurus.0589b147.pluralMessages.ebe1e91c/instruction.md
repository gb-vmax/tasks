# Bug Report

### Describe the bug

I'm experiencing an issue with the `usePluralForm` hook where the plural message selection is not working correctly. When I try to use `selectMessage` with a count and plural messages, the wrong message is being selected or the function throws an error.

### Reproduction

```js
const { selectMessage } = usePluralForm();

// Trying to select the appropriate plural form
const message = selectMessage(5, 'one item|many items');

// Expected: "many items"
// Actual: incorrect result or error
```

The function seems to be receiving the arguments in an unexpected way, causing the plural form selection logic to fail.

### Expected behavior

The `selectMessage` function should correctly select the appropriate plural form based on the count and the locale's plural rules. For example, with a count of 5 and messages like "one item|many items", it should return "many items" for English locale.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
