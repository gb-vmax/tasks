# Bug Report

### Describe the bug

The Slider component's keyboard navigation is broken when using arrow keys to jump between marks. When pressing the right arrow key to move to the next mark, the slider jumps to the previous mark instead. The navigation behavior is completely reversed from what it should be.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  const marks = [
    { value: 20, label: '20%' },
    { value: 50, label: '50%' },
    { value: 80, label: '80%' }
  ];

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
1. Create a Slider with marks at positions 20, 50, and 80
2. Set the initial value to 20
3. Press the right arrow key to move to the next mark
4. The slider moves to 50, but it should move forward to the next mark

The slider seems to be navigating in the wrong direction when using keyboard controls to jump between marks.

### Expected behavior

When pressing the right arrow key, the slider should move to the next mark with a higher value. Currently it appears to be doing the opposite.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
