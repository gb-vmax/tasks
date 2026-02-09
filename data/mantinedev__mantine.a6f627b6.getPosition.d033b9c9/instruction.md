# Bug Report

### Describe the bug

The Slider component is displaying values in reverse - when I set a value closer to the max, the slider thumb appears closer to the min position, and vice versa. The visual position of the slider thumb is inverted compared to its actual value.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState(75);
  
  return (
    <Slider 
      min={0} 
      max={100} 
      value={value}
      onChange={setValue}
    />
  );
}
```

When the value is set to 75, the slider thumb appears at the 25% position instead of 75%. Similarly, a value of 25 shows the thumb at 75%.

### Expected behavior

The slider thumb should be positioned at 75% when the value is 75 (with min=0 and max=100). Higher values should move the thumb towards the right/top, and lower values towards the left/bottom.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
