# Bug Report

### Describe the bug

I'm experiencing an issue with comma or space separated value parsing. When I pass a string with comma-separated or space-separated values, I'm getting back an empty array instead of the parsed values.

### Reproduction

```js
// Both of these return empty arrays when they shouldn't
const result1 = commaOrSpaceSeparated('item1,item2,item3');
const result2 = commaOrSpaceSeparated('item1 item2 item3');

console.log(result1); // Expected: ['item1', 'item2', 'item3'], Got: []
console.log(result2); // Expected: ['item1', 'item2', 'item3'], Got: []
```

### Expected behavior

The function should parse comma-separated and space-separated strings and return an array containing the individual items. Empty items should be filtered out, but valid items should be preserved.

### Additional context

This seems to have started happening recently. The function is supposed to handle both comma-separated and space-separated formats, but currently returns empty arrays for both cases.

---
Repository: /testbed
