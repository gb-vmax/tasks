# Bug Report

### Describe the bug

I'm experiencing an issue with virtual colors where the CSS variable references are off by one. When using `virtualColor()` to create a color tuple, the generated CSS variables start at index 1 instead of 0, which doesn't match the expected color shade indices.

### Reproduction

```js
const myVirtualColor = virtualColor({
  name: 'custom',
  dark: 'blue',
  light: 'cyan'
});

// Checking the generated CSS variable references
console.log(myVirtualColor[0]); // Expected: var(--mantine-color-custom-0)
                                 // Actual: var(--mantine-color-custom-1)
console.log(myVirtualColor[9]); // Expected: var(--mantine-color-custom-9)
                                 // Actual: var(--mantine-color-custom-10)
```

This causes the color shades to be misaligned when the virtual color is used in components. For example, if I'm trying to reference shade 0 (the lightest shade), I'm actually getting shade 1 instead.

### Expected behavior

The virtual color tuple should generate CSS variables with indices from 0 to 9, matching the standard Mantine color tuple format where:
- Index 0 = `var(--mantine-color-{name}-0)`
- Index 1 = `var(--mantine-color-{name}-1)`
- ...
- Index 9 = `var(--mantine-color-{name}-9)`

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
