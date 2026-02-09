# Bug Report

### Describe the bug

The plural form selection is not working correctly when using the `usePluralForm` utility. The wrong message variant is being selected based on the count value.

### Reproduction

```js
// Example with English locale
const messages = "one item|many items";
const count = 1;

// Expected: "one item"
// Actual: "many items"
```

When I pass a count that should select the first plural form (e.g., count=1 for singular in English), it's returning the wrong message variant. It seems like the index calculation is off by one.

Also noticed that if my plural messages contain a pipe character (`|`) as part of the actual text content, the splitting logic breaks and uses a different separator, which causes even more confusion.

### Expected behavior

The correct plural form message should be selected based on the count and locale rules. For example:
- count=1 should return the singular form
- count=2+ should return the plural form (for English)

The separator logic should be consistent and not change based on message content.

### System Info
- Docusaurus version: latest
- Theme: docusaurus-theme-common

---
Repository: /testbed
