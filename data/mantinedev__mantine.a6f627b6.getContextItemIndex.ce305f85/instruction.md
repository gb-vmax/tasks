# Bug Report

### Describe the bug

The `getContextItemIndex` function is not correctly finding the index of an element within its parent context. It seems to be searching in the wrong scope and using an incorrect comparison method.

### Reproduction

```js
// Given a DOM structure like:
// <div class="parent">
//   <button class="item">First</button>
//   <button class="item">Second</button>
//   <button class="item">Third</button>
// </div>

const button = document.querySelector('.item:nth-child(2)');
const index = getContextItemIndex(button, '.parent', '.item');

// Expected: 1 (second item, 0-indexed)
// Actual: Returns incorrect index or -1
```

### Expected behavior

The function should:
1. Find the parent element matching the `parentSelector`
2. Query all child elements matching the `elementSelector` within that parent
3. Return the index of the current node in that list

Currently it's not traversing up to find the parent element correctly, and the element comparison logic seems off.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
