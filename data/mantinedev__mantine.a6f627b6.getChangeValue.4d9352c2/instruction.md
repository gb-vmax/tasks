# Bug Report

### Describe the bug

I'm experiencing an issue with the Slider component where the value calculation seems off when dragging the slider handle. The slider is not respecting the maximum value boundary correctly and the position-to-value conversion appears to be incorrect.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState(50);
  
  return (
    <Slider
      min={0}
      max={100}
      step={1}
      value={value}
      onChange={setValue}
    />
  );
}
```

Steps to reproduce:
1. Create a slider with min=0, max=100
2. Drag the slider handle to the maximum position
3. The value doesn't reach the maximum correctly
4. Also, the initial position calculation seems to be off by a small amount

### Expected behavior

- When dragging the slider handle to the far right, it should set the value to the maximum (100)
- The position-to-value conversion should accurately reflect the handle position
- The value should stay within the min/max boundaries at all times

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

This is affecting my forms where users need to select precise values using the slider. Any help would be appreciated!

---
Repository: /testbed
