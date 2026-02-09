# Bug Report

### Describe the bug

I'm experiencing an issue with ResizeObserver in my application. When multiple resize events occur in quick succession, some of the observer callbacks are being skipped and not triggered. This is causing layout issues where components don't properly respond to size changes.

### Reproduction

```js
const element = document.createElement('div');
const observer = new ResizeObserver((entries) => {
  console.log('Resize detected:', entries);
});

observer.observe(element);

// Simulate multiple rapid resize events
for (let i = 0; i < 10; i++) {
  element.style.width = `${100 + i}px`;
}

// Expected: 10 console logs
// Actual: Only ~5 console logs appear
```

### Expected behavior

All resize observer callbacks should be triggered when the observed element changes size. Each callback should fire exactly once per resize event.

### Additional context

This seems to happen specifically when there are multiple resize events happening rapidly. Single resize events work fine, but when batched together, some callbacks are mysteriously skipped.

---
Repository: /testbed
