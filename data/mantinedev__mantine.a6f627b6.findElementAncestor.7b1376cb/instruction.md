# Bug Report

### Describe the bug

The `findElementAncestor` utility function is not working as expected. When trying to find an ancestor element that matches a specific selector, it returns the wrong element or `null` even when a matching ancestor exists in the DOM tree.

### Reproduction

```js
// HTML structure:
// <div class="container">
//   <div class="wrapper">
//     <button id="myButton">Click me</button>
//   </div>
// </div>

const button = document.getElementById('myButton');
const ancestor = findElementAncestor(button, '.container');

// Expected: Returns the div with class "container"
// Actual: Returns null or unexpected element
```

### Steps to reproduce:
1. Create a nested DOM structure with multiple parent elements
2. Call `findElementAncestor` on a child element with a selector that matches one of its ancestors
3. The function doesn't return the expected ancestor element

### Expected behavior

The function should traverse up the DOM tree and return the first ancestor element that matches the provided selector. If I have a button nested inside a container div, calling `findElementAncestor(button, '.container')` should return that container div.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
