# Bug Report

### Describe the bug

The `cssObjectToString` function is producing malformed CSS strings with incorrect semicolon placement. When converting CSS objects to strings, the semicolons are appearing at the beginning of each property instead of at the end, which breaks the CSS syntax.

Additionally, CSS properties with falsy values (like `0`, empty strings, etc.) are now being skipped entirely, which is incorrect behavior since `0` is a valid CSS value.

### Reproduction

```js
import { cssObjectToString } from '@mantine/core';

// Example 1: Semicolons in wrong position
const css1 = cssObjectToString({
  color: 'red',
  fontSize: '16px'
});
console.log(css1);
// Output: ";color:red;font-size:16px" (incorrect - starts with semicolon)
// Expected: "color:red;font-size:16px;"

// Example 2: Valid falsy values being ignored
const css2 = cssObjectToString({
  margin: 0,
  padding: '10px'
});
console.log(css2);
// Output: ";padding:10px" (margin: 0 is missing)
// Expected: "margin:0;padding:10px;"
```

### Expected behavior

1. Semicolons should appear at the end of each CSS property, not at the beginning
2. Falsy values like `0` should not be filtered out, as they are valid CSS values
3. The resulting CSS string should be properly formatted and ready to use in style attributes

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
