# Bug Report

### Describe the bug

The Slider component's keyboard navigation is behaving incorrectly when jumping between marks. When pressing the arrow keys to move to the next mark, the slider jumps to the wrong mark or doesn't move at all.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

const marks = [
  { value: 20, label: '20%' },
  { value: 50, label: '50%' },
  { value: 80, label: '80%' }
];

function Demo() {
  return (
    <Slider
      defaultValue={20}
      marks={marks}
      step={10}
    />
  );
}
```

Steps to reproduce:
1. Create a Slider with multiple marks
2. Set the initial value to one of the marks (e.g., 20)
3. Try to navigate to the next mark using keyboard arrows
4. The slider jumps to an unexpected value or stays at the current position

### Expected behavior

When navigating with keyboard, the slider should move to the next mark in ascending order (20 → 50 → 80), not jump backwards or stay in place.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
