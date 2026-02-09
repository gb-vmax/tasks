# Bug Report

### Describe the bug

I'm experiencing an issue with `getComputedStyle` where it returns stale/cached values when called on different elements. After the first call, subsequent calls to `getComputedStyle` with different elements return the same computed style object instead of computing styles for the new element.

### Reproduction

```js
const element1 = document.createElement('div');
element1.style.color = 'red';

const element2 = document.createElement('div');
element2.style.color = 'blue';

const styles1 = window.getComputedStyle(element1);
const styles2 = window.getComputedStyle(element2);

// Both return the same cached result
console.log(styles1.color); // Expected: 'red'
console.log(styles2.color); // Expected: 'blue', but returns 'red'
```

### Expected behavior

Each call to `getComputedStyle` should return the computed styles for the specific element passed to it, not a cached result from a previous call.

### Additional context

This seems to have started happening recently. The function appears to be caching the result from the first call and returning it for all subsequent calls regardless of which element is passed in.

---
Repository: /testbed
