# Bug Report

### Describe the bug

I'm experiencing incorrect behavior with the Slider component when dragging or clicking to change values. The slider value calculation seems completely off - values are either way too large or not respecting the min/max boundaries properly.

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

When I click or drag the slider:
1. The values returned don't match where I clicked on the slider track
2. Values seem to exceed the max value or don't respect the boundaries
3. The calculation appears to be multiplying instead of dividing somewhere

### Expected behavior

The slider should:
- Return values proportional to the click/drag position on the track
- Respect the min and max boundaries
- Calculate the value correctly based on the container width and position

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

This seems like a calculation issue in the value conversion logic. The slider was working fine in previous versions.

---
Repository: /testbed
