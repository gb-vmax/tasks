# Bug Report

### Describe the bug

When using theme class names with multiple theme components, the class name resolution is not working correctly. It seems like the function is trying to access a selector property on the result, but this causes issues when the resolved value is undefined or null.

### Reproduction

```js
// Set up a component with multiple theme names
const themeNames = ['Button', 'Input'];

// Try to get class names for a specific selector
const classNames = getThemeClassNames({
  themeName: themeNames,
  selector: 'root',
  theme,
  props,
  stylesCtx
});

// Expected: array of class names
// Actual: array containing undefined values
```

### Expected behavior

The function should return an array of resolved class names from all theme components. When a theme component doesn't have class names defined, it should be handled gracefully without adding undefined values to the result array.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
