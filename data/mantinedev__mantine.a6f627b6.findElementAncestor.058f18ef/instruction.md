# Bug Report

### Describe the bug

The `findElementAncestor` utility function is not working correctly - it's returning the wrong element when searching for ancestor elements by selector. It seems to be returning elements that don't match the selector instead of the ones that do.

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
// Actual: Returns null or wrong element
```

### Steps to reproduce:
1. Create a nested DOM structure with specific class names
2. Call `findElementAncestor` on a child element with a selector matching a parent
3. The function returns `null` or an incorrect element instead of the matching ancestor

### Expected behavior

The function should traverse up the DOM tree and return the first ancestor element that matches the provided selector. If no matching ancestor is found, it should return `null`.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
