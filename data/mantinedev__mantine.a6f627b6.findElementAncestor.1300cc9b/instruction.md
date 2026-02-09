# Bug Report

### Describe the bug

The `findElementAncestor` utility function is not correctly finding ancestor elements that match a given selector. It appears to be skipping the immediate parent and returning incorrect results.

### Reproduction

```js
// HTML structure:
// <div class="grandparent">
//   <div class="parent">
//     <div class="child"></div>
//   </div>
// </div>

const childElement = document.querySelector('.child');
const result = findElementAncestor(childElement, '.parent');

// Expected: returns the .parent div
// Actual: returns null or wrong element
```

### Expected behavior

The function should traverse up the DOM tree starting from the element's parent and return the first ancestor that matches the provided selector. In the example above, it should find and return the `.parent` element.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
