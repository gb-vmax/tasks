# Bug Report

### Describe the bug

The RangeSlider component is not displaying labels correctly. When I use the RangeSlider, the thumb labels appear empty/blank instead of showing the actual values.

### Reproduction

```jsx
import { RangeSlider } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState([20, 80]);
  
  return (
    <RangeSlider
      value={value}
      onChange={setValue}
      min={0}
      max={100}
    />
  );
}
```

When dragging the slider thumbs, the labels that appear above them are blank. They should display the current numeric values (e.g., "20" and "80").

### Expected behavior

The labels should display the current slider values. For example, if the range is [20, 80], hovering over or dragging the thumbs should show "20" and "80" in the labels.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
