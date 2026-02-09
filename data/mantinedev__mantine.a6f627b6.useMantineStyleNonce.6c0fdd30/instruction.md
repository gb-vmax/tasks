# Bug Report

### Describe the bug

The `useMantineStyleNonce` hook is returning a function instead of the actual nonce value. This causes issues when trying to use the nonce for inline styles or CSP headers.

### Reproduction

```tsx
import { useMantineStyleNonce } from '@mantine/core';

function MyComponent() {
  const nonce = useMantineStyleNonce();
  
  console.log(nonce); // Logs: [Function: getStyleNonce]
  console.log(typeof nonce); // Logs: "function"
  
  // This doesn't work as expected
  return <style nonce={nonce}>...</style>
}
```

### Expected behavior

The hook should return the actual nonce string value, not the getter function. It should work like:

```tsx
const nonce = useMantineStyleNonce();
console.log(nonce); // Should log: "abc123" (or whatever the nonce value is)
console.log(typeof nonce); // Should log: "string"
```

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
