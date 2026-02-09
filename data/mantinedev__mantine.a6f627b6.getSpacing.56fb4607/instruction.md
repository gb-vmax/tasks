# Bug Report

### Describe the bug

The `getSpacing` utility function is returning incorrect CSS variable names. When I use spacing values in my components, the generated CSS variables have the wrong prefix and the values aren't being applied correctly.

### Reproduction

```js
import { getSpacing } from '@mantine/core';

// Expected: var(--mantine-spacing-md)
// Actual: returns something different
const spacing = getSpacing('md');
console.log(spacing);
```

When using spacing props on Mantine components, the styles don't get applied properly. For example:

```jsx
<Box p="md" m="lg">
  Content here
</Box>
```

The padding and margin values aren't being calculated correctly and the component doesn't have the expected spacing.

### Expected behavior

The `getSpacing` function should generate CSS variables with the `--mantine-spacing-*` prefix and correctly handle string size values like 'xs', 'sm', 'md', 'lg', 'xl', as well as numeric values.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
