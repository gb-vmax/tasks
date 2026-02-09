# Bug Report

### Describe the bug

The RingProgress component is throwing an error when rendering with certain section configurations. It appears that the component is trying to access an array element that doesn't exist, causing `undefined` to be passed where a valid section object is expected.

### Reproduction

```jsx
import { RingProgress } from '@mantine/core';

function Demo() {
  return (
    <RingProgress
      sections={[
        { value: 40, color: 'cyan' },
        { value: 25, color: 'orange' },
        { value: 15, color: 'grape' }
      ]}
    />
  );
}
```

When the component renders, it crashes with an error related to accessing properties on `undefined`. This seems to happen when the internal curve calculation logic tries to process the sections array.

### Expected behavior

The RingProgress component should render correctly with the provided sections without any errors. Each section should be displayed as a segment of the ring with the appropriate colors and values.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
