# Bug Report

### Describe the bug

I'm experiencing an issue with element ancestor traversal where `findElementAncestor` is not returning the correct ancestor element when searching up the DOM tree. The function seems to get stuck in an infinite loop or returns unexpected results when trying to find a parent element matching a specific selector.

### Reproduction

```js
const childElement = document.querySelector('.child');
const ancestor = findElementAncestor(childElement, '.parent-class');

// Expected: Should return the ancestor element with class 'parent-class'
// Actual: Function hangs or returns null even when ancestor exists
```

HTML structure:
```html
<div class="parent-class">
  <div class="intermediate">
    <div class="child">Content</div>
  </div>
</div>
```

### Expected behavior

The function should traverse up the DOM tree and return the first ancestor element that matches the provided selector. If no matching ancestor is found, it should return `null`.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
