# Bug Report

### Describe the bug

I'm experiencing an issue with CSS value validation in Mantine components. It seems like certain valid CSS values are being rejected or incorrectly validated, while some invalid values are being accepted.

### Reproduction

```js
// These CSS calc() expressions should be valid but aren't working:
<Box style={{ width: 'calc(100% - 20px)' }} />

// Also having issues with CSS variables:
<Box style={{ width: 'var(--my-width)' }} />

// Multi-value properties with spaces seem to behave incorrectly:
<Box style={{ padding: '10px 20px' }} />
```

### Expected behavior

- CSS `calc()` expressions should be recognized as valid numeric-like values
- CSS `var()` expressions should be recognized as valid numeric-like values  
- Multi-value CSS properties (like `10px 20px` for padding) should be properly validated
- Invalid values should be rejected while valid CSS values should be accepted

### System Info

- @mantine/core version: latest
- Browser: Chrome

This is affecting multiple components that accept size/spacing props. Any help would be appreciated!

---
Repository: /testbed
