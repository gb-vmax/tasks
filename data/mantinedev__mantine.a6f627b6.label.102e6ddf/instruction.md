# Bug Report

### Describe the bug

The Slider component is throwing an error when trying to display labels. It seems like the default label formatter is trying to call the value as a function, which causes a runtime error since the value is typically a number.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      defaultValue={50}
      min={0}
      max={100}
    />
  );
}
```

When the slider is rendered and you try to interact with it (hover or drag), you'll get an error like `f is not a function` or similar, because the label formatter is attempting to call the numeric value as if it were a function.

### Expected behavior

The slider should display the numeric value as the label without any errors. The default label formatter should simply return the value passed to it, not try to invoke it as a function.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
