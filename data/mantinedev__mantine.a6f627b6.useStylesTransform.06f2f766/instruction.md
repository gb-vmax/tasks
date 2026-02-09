# Bug Report

### Describe the bug

When using components with multiple theme names (e.g., compound components), only the first theme name's styles are being applied instead of all theme names in the array. This causes styles from secondary theme names to be ignored.

### Reproduction

```jsx
// Component with multiple theme names
const MyCompoundComponent = () => {
  // Internally uses themeName = ['PrimaryComponent', 'SecondaryComponent']
  return <div>Content</div>
}

// Theme configuration
const theme = {
  components: {
    PrimaryComponent: {
      styles: { root: { color: 'red' } }
    },
    SecondaryComponent: {
      styles: { root: { background: 'blue' } }
    }
  }
}
```

### Expected behavior

Both `PrimaryComponent` and `SecondaryComponent` styles should be applied to the component. The component should have both the red color and blue background.

### Actual behavior

Only the styles from `PrimaryComponent` (the first theme name) are applied. The `SecondaryComponent` styles are completely ignored.

This seems to have broken recently and is affecting all compound components that rely on multiple theme names for their styling.

---
Repository: /testbed
