# Bug Report

### Describe the bug

I'm experiencing an issue with comma-separated attribute parsing in MDX. It appears that the `commaSeparated` function is now splitting values on semicolons (`;`) instead of commas (`,`), which breaks the expected behavior for parsing comma-separated lists.

### Reproduction

```js
// Expected: values should be split by commas
const input = "value1, value2, value3";
const result = commaSeparated(input);

// Currently returns: ["value1, value2, value3"] (split by semicolon)
// Expected: ["value1", "value2", "value3"] (split by comma)
```

When processing MDX attributes that should accept comma-separated values, the parser is not splitting them correctly. For example:

```mdx
<Component items="apple, banana, orange" />
```

The items are not being parsed into separate values as expected.

### Expected behavior

The `commaSeparated` function should split strings on commas (`,`) not semicolons (`;`). Comma-separated values are a standard format and changing the delimiter breaks compatibility with existing MDX content and common use cases.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like it might have been introduced in a recent change. The function name clearly indicates it should handle comma-separated values, but the implementation is using the wrong delimiter.

---
Repository: /testbed
