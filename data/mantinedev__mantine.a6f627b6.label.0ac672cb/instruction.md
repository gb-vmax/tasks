# Bug Report

### Describe the bug

The Slider component's label formatter is not displaying labels correctly anymore. When I pass a custom label function or use the default behavior, the labels either don't show up or display incorrectly.

### Reproduction

```jsx
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      defaultValue={50}
      marks={[
        { value: 20, label: '20%' },
        { value: 50, label: '50%' },
        { value: 80, label: '80%' },
      ]}
    />
  );
}
```

When using the slider, the labels on the marks don't appear as expected. Also tried with a custom label function:

```jsx
<Slider
  defaultValue={50}
  label={(value) => `${value}°C`}
/>
```

The tooltip label doesn't format properly when dragging the thumb.

### Expected behavior

- Mark labels should display correctly with the text specified
- Custom label formatter functions should work and format the tooltip value as expected
- Default label behavior should show the numeric value

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
