# Bug Report

### Describe the bug

The `toKebabCase` function is not converting strings with multiple spaces correctly. When a string contains multiple consecutive spaces, only the first space gets replaced with a hyphen, leaving the remaining spaces unconverted.

### Reproduction

```js
import { toKebabCase } from './misc';

// This doesn't work as expected
const result = toKebabCase('hello  world  test');
console.log(result); // Outputs: "hello- world- test"
// Expected: "hello-world-test"

// Another example
const result2 = toKebabCase('foo   bar');
console.log(result2); // Outputs: "foo-  bar"
// Expected: "foo-bar"
```

### Expected behavior

All spaces in the string should be replaced with hyphens, not just the first occurrence in each sequence. The function should handle multiple consecutive spaces correctly.

### System Info

- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
