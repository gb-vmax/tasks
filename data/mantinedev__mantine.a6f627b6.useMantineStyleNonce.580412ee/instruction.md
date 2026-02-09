# Bug Report

### Describe the bug

The `useMantineStyleNonce` hook is returning an unexpected object structure instead of the nonce value directly. This breaks components that expect to receive the nonce function or value directly from the hook.

### Reproduction

```tsx
import { useMantineStyleNonce } from '@mantine/core';

function MyComponent() {
  const styleNonce = useMantineStyleNonce();
  
  // This no longer works as expected
  // Previously: styleNonce would be a function
  // Now: styleNonce is { nonce: <value> }
  
  console.log(typeof styleNonce); // Expected: 'function', Actual: 'object'
}
```

### Expected behavior

The hook should return the `getStyleNonce` function directly, not wrapped in an object. Components relying on this hook are now receiving an unexpected data structure.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
