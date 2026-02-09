# Bug Report

### Describe the bug

After a recent update, calling `scrollIntoView()` with an options object throws an error saying "scrollIntoView options not supported". This breaks existing code that was working fine before.

### Reproduction

```js
const element = document.getElementById('myElement');

// This now throws an error
element.scrollIntoView({ behavior: 'smooth', block: 'center' });

// Error: scrollIntoView options not supported
```

### Expected behavior

The `scrollIntoView()` method should accept an options object (or at minimum not throw an error when one is passed). This is standard DOM API behavior and was working in previous versions.

### Additional context

Calling `scrollIntoView()` without arguments still works:
```js
element.scrollIntoView(); // Works fine
```

But any attempt to pass options causes the error. This is blocking our smooth scrolling functionality.

---
Repository: /testbed
