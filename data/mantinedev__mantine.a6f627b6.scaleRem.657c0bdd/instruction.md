# Bug Report

### Describe the bug

I'm experiencing an issue with the `rem()` utility function in Mantine. When using `rem()` with non-zero values, the generated CSS output appears to be malformed and breaks styling. The styles are not being applied correctly in the browser.

### Reproduction

```js
import { rem } from '@mantine/core';

// This produces invalid CSS
const spacing = rem(16);
console.log(spacing); // Expected valid CSS calc expression

// Using it in a component
<Box style={{ padding: rem(20) }}>
  Content
</Box>
```

The generated CSS string seems to be incomplete and causes the browser to ignore the style rule entirely.

### Expected behavior

The `rem()` function should generate valid CSS calc expressions that work with Mantine's scaling system. For example, `rem(16)` should produce something like `calc(1rem * var(--mantine-scale))`.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
