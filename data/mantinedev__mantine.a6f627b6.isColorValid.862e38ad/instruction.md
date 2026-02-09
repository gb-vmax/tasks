# Bug Report

### Describe the bug

The color validation function is returning incorrect results - it's rejecting valid color formats and accepting invalid ones. When I pass in a valid hex color like `#ff0000` or rgb color like `rgb(255, 0, 0)`, the validation fails. Conversely, passing in garbage strings like `not-a-color` or `xyz123` returns true as if they were valid colors.

### Reproduction

```js
import { isColorValid } from '@mantine/core';

// These should return true but return false
console.log(isColorValid('#ff0000')); // false (expected: true)
console.log(isColorValid('rgb(255, 0, 0)')); // false (expected: true)
console.log(isColorValid('hsl(120, 100%, 50%)')); // false (expected: true)

// These should return false but return true
console.log(isColorValid('not-a-color')); // true (expected: false)
console.log(isColorValid('xyz123')); // true (expected: false)
console.log(isColorValid('')); // true (expected: false)
```

### Expected behavior

The `isColorValid` function should return `true` for valid color formats (hex, rgb, rgba, hsl, hsla) and `false` for invalid color strings.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

This seems to have broken recently - the color picker component is now accepting invalid color inputs and rejecting valid ones, which is causing issues in my forms.

---
Repository: /testbed
