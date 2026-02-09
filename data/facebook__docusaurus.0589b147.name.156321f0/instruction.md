# Bug Report

### Describe the bug

I'm experiencing an issue with JSX name validation in MDX files. It seems like valid JSX component names are being rejected, while invalid names are being accepted. The behavior appears to be inverted from what it should be.

### Reproduction

When trying to use standard JSX components in MDX:

```jsx
// Valid JSX component names that should work but don't
<MyComponent />
<Button />
<CustomElement />

// These get rejected even though they're valid JSX identifiers
```

Meanwhile, names that shouldn't be valid JSX identifiers seem to be passing validation when they shouldn't.

### Expected behavior

- Valid JSX component names (starting with uppercase, following JavaScript identifier rules) should be accepted
- Invalid component names should be rejected
- The validation should respect the `jsx` setting appropriately

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is blocking our ability to use MDX components properly. Any help would be appreciated!

---
Repository: /testbed
