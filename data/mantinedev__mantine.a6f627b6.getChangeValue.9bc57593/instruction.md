# Bug Report

### Describe the bug

I'm experiencing an issue with the Slider component where dragging the slider handle produces incorrect values. The slider seems to calculate the wrong position when I try to set a value by clicking or dragging.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState(50);
  
  return (
    <Slider
      value={value}
      onChange={setValue}
      min={0}
      max={100}
      step={1}
    />
  );
}
```

When I drag the slider or click on different positions:
- Clicking near the start of the slider sets unexpected values
- Dragging the handle doesn't follow the cursor properly
- The value calculation seems completely off

### Expected behavior

The slider should:
1. Calculate the correct value based on the click/drag position
2. The handle should follow the cursor smoothly
3. Values should be properly constrained between min and max

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
