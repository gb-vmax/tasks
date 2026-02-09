# Bug Report

### Describe the bug

I'm experiencing an issue with the `getContextItemIndex` utility function where it always returns `0` for any element, regardless of its actual position in the list. This is causing problems with keyboard navigation and focus management in components that rely on this utility.

### Reproduction

```js
// Given a DOM structure like:
// <div class="parent">
//   <button class="item">First</button>
//   <button class="item">Second</button>
//   <button class="item">Third</button>
// </div>

const secondButton = document.querySelector('.item:nth-child(2)');
const index = getContextItemIndex('.parent', '.item', secondButton);

// Expected: 1
// Actual: 0
```

The function returns `0` for all elements instead of their correct index position. This breaks functionality where the element's position matters, like in dropdown menus, tab lists, or any component that needs to track which item is currently focused.

### Expected behavior

The function should return the correct index of the element within its parent container. For example:
- First element should return `0`
- Second element should return `1`
- Third element should return `2`
- etc.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox (reproduced on both)

---
Repository: /testbed
