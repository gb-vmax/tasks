# Bug Report

### Describe the bug

I'm experiencing issues with the styles API when passing an array of styles to a component. The styles don't seem to be applied correctly and the component either doesn't render with any styles or throws an error.

### Reproduction

```tsx
import { Button } from '@mantine/core';

const customStyles = [
  { root: { backgroundColor: 'red' } },
  { root: { color: 'white' } }
];

// This doesn't work as expected
<Button styles={customStyles}>
  Click me
</Button>
```

When passing an array of style objects, I expect them to be merged together and applied to the component, but instead the styles are either not applied at all or the component breaks.

### Expected behavior

When providing an array of styles, they should be properly merged and applied to the component. Each style object in the array should be combined in order, with later styles overriding earlier ones where properties conflict.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
