# Bug Report

### Slider component displays incorrect values with negative numbers

I'm experiencing an issue with the Slider component where negative values are not being displayed or handled correctly. When I set a slider to use negative values, the displayed value seems to be the absolute value instead of preserving the sign.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState(-5);
  
  return (
    <Slider
      value={value}
      onChange={setValue}
      min={-10}
      max={10}
      precision={2}
    />
  );
}
```

When I drag the slider to the left (negative values), the component shows positive values instead. For example, if I set the value to -5.5, it displays as 5.5.

### Expected behavior

The slider should correctly display and handle negative values. If the value is -5.5, it should show -5.5, not 5.5.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
