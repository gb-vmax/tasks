# Bug Report

### Describe the bug

When using floating components (tooltips, popovers, etc.) with RTL (right-to-left) direction, the positioning logic seems broken. The floating element appears in unexpected positions, and even LTR components with 'right' or 'left' positions are being affected when they shouldn't be.

### Reproduction

```js
// RTL with right position
getFloatingPosition('rtl', 'right-start')
// Expected: 'left-start'
// Actual: incorrect position

// LTR with right position - this shouldn't be flipped at all
getFloatingPosition('ltr', 'right-start')
// Expected: 'right-start' (unchanged)
// Actual: position gets modified incorrectly
```

### Expected behavior

- Only RTL direction should trigger position flipping for left/right positions
- LTR direction should never flip positions
- When flipping occurs, the format should be `${side}-${placement}`, not `${placement}-${side}`

### System Info

- Mantine version: latest
- Direction: RTL and LTR both affected

---
Repository: /testbed
