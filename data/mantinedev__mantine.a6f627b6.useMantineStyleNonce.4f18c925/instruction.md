# Bug Report

### Describe the bug

The `useMantineStyleNonce` hook is returning a function instead of the actual nonce value. When trying to use the nonce in components, I'm getting a function reference rather than the string/undefined value I expect.

### Reproduction

```jsx
import { useMantineStyleNonce } from '@mantine/core';

function MyComponent() {
  const nonce = useMantineStyleNonce();
  
  console.log(typeof nonce); // logs "function" instead of "string" or "undefined"
  
  // This doesn't work as expected
  return <style nonce={nonce}>...</style>;
}
```

### Expected behavior

The hook should return the actual nonce value (string or undefined), not the getter function itself. The nonce should be usable directly in component props.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
