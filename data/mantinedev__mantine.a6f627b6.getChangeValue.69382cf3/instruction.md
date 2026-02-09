# Bug Report

### Describe the bug

I'm experiencing an issue with the Slider component where dragging the slider handle produces incorrect values. The slider seems to be calculating position values incorrectly, resulting in unexpected behavior when trying to set values by clicking or dragging.

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
1. The slider handle moves to unexpected positions
2. The value calculated doesn't correspond to where I clicked on the track
3. Values seem to be clamped incorrectly

### Expected behavior

The slider should:
- Calculate the correct value based on the click/drag position
- Move the handle to the position where the user clicks
- Return values that correspond to the actual position on the slider track

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
