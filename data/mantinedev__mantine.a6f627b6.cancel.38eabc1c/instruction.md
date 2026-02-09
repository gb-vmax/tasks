# Bug Report

### Describe the bug

The `cancel()` method on the debounced callback is throwing an error instead of silently canceling the operation. When I call `cancel()` on a debounced function, my application crashes with an uncaught error.

### Reproduction

```js
import { useDebouncedCallback } from '@mantine/hooks';

const debouncedFn = useDebouncedCallback(() => {
  console.log('This should not execute');
}, 500);

// Schedule the debounced function
debouncedFn();

// Try to cancel it
debouncedFn.cancel(); // Error: Operation cancelled
```

### Expected behavior

The `cancel()` method should silently cancel any pending debounced callbacks without throwing an error. This is the standard behavior for debounce implementations (like lodash's debounce) where canceling is a normal operation that shouldn't disrupt the application flow.

### System Info

- @mantine/hooks version: latest
- React version: 18.x
- Node: 18.x

---
Repository: /testbed
