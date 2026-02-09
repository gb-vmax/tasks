# Bug Report

### Describe the bug
The `getFontSize` utility is not returning the correct font size values. When I try to use font size props on components, the sizes don't match what's defined in the theme and I'm getting unexpected values instead.

### Reproduction
```tsx
import { getFontSize } from '@mantine/core';

// Expected: returns the actual font size from theme
const fontSize = getFontSize('md');
console.log(fontSize); // Getting wrong value

// This affects components that use font sizes
<Text size="md">This text has incorrect font size</Text>
```

### Expected behavior
The function should return the correct font size value from the theme based on the size token passed in (e.g., 'xs', 'sm', 'md', 'lg', 'xl').

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
