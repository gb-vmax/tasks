# Bug Report

### Describe the bug

Keyboard navigation is not working correctly in RTL (right-to-left) mode. When using arrow keys to navigate through elements, the direction is reversed - pressing ArrowRight moves to the previous element instead of the next one, and ArrowLeft moves to the next element instead of the previous one.

Additionally, Home and End keys are focusing on disabled elements instead of skipping them.

### Reproduction

```js
// Set up a component with RTL direction
<div dir="rtl">
  <Button>First</Button>
  <Button>Second</Button>
  <Button>Third</Button>
</div>

// When pressing ArrowRight, focus moves to the previous button (left)
// When pressing ArrowLeft, focus moves to the next button (right)
// This is backwards - ArrowRight should move right (which is previous in RTL)
```

For the Home/End issue:
```js
<div>
  <Button disabled>First (disabled)</Button>
  <Button>Second</Button>
  <Button>Third</Button>
</div>

// Pressing Home focuses on the disabled first button
// Expected: Should skip disabled elements and focus on the second button
```

### Expected behavior

- In RTL mode, ArrowRight should move to the visually right element (which is the previous element in the array)
- In RTL mode, ArrowLeft should move to the visually left element (which is the next element in the array)
- Home key should focus on the first non-disabled element
- End key should focus on the last non-disabled element

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
