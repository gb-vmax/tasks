# Bug Report

### Describe the bug

I'm experiencing an issue with JSX name validation in MDX. It seems like the logic for determining which regex pattern to use is reversed - when `jsx: true` is passed in options, it's using the wrong validation pattern, and vice versa.

### Reproduction

```js
// When jsx option is true, non-JSX names are accepted
const options = { jsx: true };
name('invalid-jsx-name', options); // Should fail JSX validation but passes

// When jsx option is false (or not set), JSX names fail validation
name('validJsxName', {}); // Should pass non-JSX validation but fails
```

### Expected behavior

When `jsx: true` is set in options, the JSX regex pattern (`nameReJsx`) should be used for validation. When `jsx: false` or not set, the standard name regex (`nameRe`) should be used.

Currently it appears to be doing the opposite - `jsx: true` uses `nameRe` and `jsx: false` uses `nameReJsx`.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
