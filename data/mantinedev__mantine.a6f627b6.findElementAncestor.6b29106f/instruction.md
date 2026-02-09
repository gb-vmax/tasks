# Bug Report

### Describe the bug

The `findElementAncestor` utility function is not working as expected. When trying to find an ancestor element that matches a specific selector, the function returns the wrong element or `null`.

### Reproduction

```js
const child = document.createElement('div');
const parent = document.createElement('div');
parent.className = 'target-class';
const grandparent = document.createElement('div');

grandparent.appendChild(parent);
parent.appendChild(child);

// Try to find the parent with class 'target-class'
const result = findElementAncestor(child, '.target-class');

// Expected: parent element with 'target-class'
// Actual: null or wrong element
console.log(result); // null
```

### Expected behavior

The function should traverse up the DOM tree and return the first ancestor element that matches the given selector. In the example above, it should return the `parent` element with class `target-class`.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
