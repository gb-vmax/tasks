# Bug Report

### Describe the bug

When using the Slider component with marks, the `getPreviousMarkValue` function doesn't return the correct value when the current value exactly matches a mark. Instead of returning the mark's value when they're equal, it skips over it and looks for a strictly smaller value.

### Reproduction

```js
const marks = [
  { value: 0, label: 'Start' },
  { value: 50, label: 'Middle' },
  { value: 100, label: 'End' }
];

// When currentValue is exactly 50
getPreviousMarkValue(50, marks);
// Returns 0 instead of 50
```

### Expected behavior

When the current value equals a mark value, the function should return that mark's value (50), not the previous one (0). The "previous or equal" mark should be returned, allowing the slider to snap correctly to marks when the value matches exactly.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
