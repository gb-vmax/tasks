# Bug Report

### Describe the bug

The `useDebouncedCallback` hook is throwing an unexpected error when calling the `flush()` method. This breaks any code that tries to manually flush pending debounced callbacks.

### Reproduction

```js
import { useDebouncedCallback } from '@mantine/hooks';

function MyComponent() {
  const debouncedFn = useDebouncedCallback(() => {
    console.log('Called');
  }, 500);

  // Call the debounced function
  debouncedFn();
  
  // Try to flush manually - this throws an error
  debouncedFn.flush();
}
```

### Expected behavior

Calling `flush()` should immediately execute any pending debounced callback without throwing an error. This is useful for cases where you need to ensure the callback runs immediately (e.g., before unmounting a component or on form submission).

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
