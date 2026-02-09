# Bug Report

### Describe the bug

I'm experiencing an issue with space-separated value parsing in MDX. When I have multiple consecutive spaces in a string, the parser seems to be dropping tokens or producing unexpected results.

### Reproduction

```js
// Example with multiple spaces between words
const input = "hello  world  test";
const result = spaceSeparated(input);

// Getting unexpected output - seems like spaces aren't being handled correctly
console.log(result); // Should split into ['hello', 'world', 'test']
```

Also seeing weird behavior with strings that have leading/trailing spaces:

```js
const input2 = "  value  ";
const result2 = spaceSeparated(input2);
// Not getting the expected array
```

### Expected behavior

The `spaceSeparated` function should properly split strings on whitespace and handle edge cases like:
- Multiple consecutive spaces between words
- Leading/trailing whitespace
- Empty strings or strings with only spaces

It should return an array with the individual tokens, similar to how standard string splitting works.

### System Info
- MDX version: 3.0.0
- Node version: Latest

This seems to have started happening recently. The parsing logic might have changed in the latest update?

---
Repository: /testbed
