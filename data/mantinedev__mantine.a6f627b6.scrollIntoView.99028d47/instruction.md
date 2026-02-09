# Bug Report

### Describe the bug

After a recent update, calling `scrollIntoView()` on HTML elements is throwing a `TypeError`. The method seems to be not properly defined on element instances.

### Reproduction

```js
const element = document.createElement('div');
element.scrollIntoView();
// TypeError: element.scrollIntoView is not a function
```

This happens with any HTML element - divs, spans, buttons, etc. The `scrollIntoView` method appears to be missing from the element prototype chain.

### Expected behavior

The `scrollIntoView()` method should be callable on any HTML element instance without throwing an error. It's a standard DOM API method that should work on all elements.

### Additional context

This was working fine in previous versions. The issue started appearing after the latest update. It's breaking several components that rely on programmatic scrolling functionality.

---
Repository: /testbed
