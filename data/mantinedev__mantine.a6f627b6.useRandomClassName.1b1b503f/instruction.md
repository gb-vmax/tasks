# Bug Report

### Describe the bug

The `useRandomClassName` hook is generating class names with double dashes (`--`) instead of single dashes, which is causing CSS selector issues. Additionally, the regex pattern for cleaning the ID seems to have changed and is now removing colons and regular dashes instead of the special characters it was handling before.

### Reproduction

```jsx
import { useRandomClassName } from '@mantine/core';

function MyComponent() {
  const className = useRandomClassName();
  console.log(className);
  // Expected: __m__-r1:0:
  // Actual: __m__--r10
}
```

The generated class names now have `--` prefix and the ID cleaning logic appears different, which breaks existing CSS selectors that rely on the previous format.

### Expected behavior

Class names should be generated with a single dash separator (e.g., `__m__-r1:0:`) and the regex should handle the original special characters (`:«»`) that React's `useId()` can produce.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
