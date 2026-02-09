# Bug Report

### Describe the bug

When passing multiple style objects or functions to a component's `styles` prop, the styles are being applied in the wrong order. Later styles in the array are being overridden by earlier ones instead of the other way around.

### Reproduction

```jsx
import { Button } from '@mantine/core';

<Button
  styles={[
    { root: { backgroundColor: 'red' } },
    { root: { backgroundColor: 'blue' } }
  ]}
>
  Click me
</Button>
```

In this example, the button appears red instead of blue. The second style object should take precedence and override the first one, but it's being applied in reverse order.

This also happens with style functions:

```jsx
<Button
  styles={[
    (theme) => ({ root: { padding: '10px' } }),
    (theme) => ({ root: { padding: '20px' } })
  ]}
>
  Click me
</Button>
```

The button ends up with 10px padding instead of 20px.

### Expected behavior

When multiple styles are provided in an array, later styles should override earlier ones (following the standard CSS cascade behavior). The last style in the array should have the highest priority.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
