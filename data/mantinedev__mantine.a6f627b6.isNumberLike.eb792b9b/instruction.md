# Bug Report

### Describe the bug

I'm experiencing an issue with CSS value validation where certain valid CSS strings are not being recognized correctly. Specifically, when using `var()` CSS custom properties, they are being incorrectly validated.

### Reproduction

```js
// This should be recognized as a valid CSS value but isn't
const value = 'var(--my-custom-property)';
// isNumberLike returns incorrect result

// Also noticing issues with unitless numeric strings
const numericValue = '42';
// Expected to work but behavior seems off
```

### Expected behavior

- `var(--custom-property)` should be recognized as a valid CSS value
- CSS function calls like `calc()` and `var()` should be properly handled
- Unitless numeric strings should be validated correctly

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

This seems to have started recently and is affecting component styling when using CSS custom properties. Any help would be appreciated!

---
Repository: /testbed
