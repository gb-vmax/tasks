# Bug Report

### Describe the bug
ResizeObserver mock in jsdom is throwing errors when `unobserve()` is called. Getting `Cannot read properties of undefined (reading 'element')` and similar errors during component cleanup.

### Reproduction
```js
const observer = new ResizeObserver(() => {});
const element = document.createElement('div');

observer.observe(element);
observer.unobserve(element);  // Throws error
```

The error happens because the mock implementation tries to access properties that don't exist on the observer instance. This breaks components that properly clean up their ResizeObserver instances.

### Expected behavior
`unobserve()` should work without throwing errors, just like the native ResizeObserver API. The mock should handle cases where internal state hasn't been initialized.

### System Info
- Environment: jsdom testing environment
- Node version: 18.x

---
Repository: /testbed
