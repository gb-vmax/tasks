# Bug Report

### Describe the bug

I'm encountering an issue with identifier validation in MDX when the `jsx` option is enabled. It appears that valid JavaScript identifiers are being rejected when they should be accepted, and the validation logic seems inverted.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

// This should work but fails with jsx: true
const result = await compile('export const myVar123 = "test"', {
  jsx: true
})

// Meanwhile, this works with jsx: false but shouldn't in some edge cases
const result2 = await compile('export const myVar123 = "test"', {
  jsx: false
})
```

When using `jsx: true`, valid identifiers that contain numbers or certain characters are being incorrectly flagged as invalid. The behavior is reversed from what it should be - identifiers that should be valid with JSX enabled are rejected, while the non-JSX mode accepts them.

### Expected behavior

The `jsx` option should correctly determine which identifier continuation characters are valid. Valid JavaScript/JSX identifiers should be accepted regardless of the `jsx` setting, with appropriate rules applied for each mode.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
