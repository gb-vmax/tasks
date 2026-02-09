# Bug Report

### Describe the bug

I'm experiencing an issue with virtual colors where the generated color tuple is missing one shade and the dark/light mode colors seem to be swapped.

When creating a virtual color, I'm only getting 9 color shades instead of the expected 10 (indices 0-9). The last shade (index 9) is missing from the generated CSS variables.

Additionally, when switching between light and dark modes, the colors appear inverted - the dark mode color is being used in light mode and vice versa.

### Reproduction

```js
const myVirtualColor = virtualColor({
  name: 'custom',
  light: 'blue',
  dark: 'cyan'
});

// Expected: Array with 10 elements (indices 0-9)
// Actual: Array with 9 elements (indices 0-8)
console.log(myVirtualColor.length); // Shows 9 instead of 10

// Also, when checking the dark property:
// Expected: Should return 'cyan' (the dark value)
// Actual: Returns 'blue' (the light value)
```

### Expected behavior

1. The virtual color tuple should contain all 10 color shades (CSS variables for indices 0 through 9)
2. The `dark` property should return the value passed as `dark` in the input, not the `light` value

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
