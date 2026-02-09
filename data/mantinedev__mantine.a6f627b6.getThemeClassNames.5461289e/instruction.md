# Bug Report

### Describe the bug

When using components with theme class names, I'm getting incorrect class name resolution. It seems like the system is trying to access class names directly on the resolver result instead of looking at the nested `classNames` property.

### Reproduction

```tsx
const theme = {
  components: {
    Button: {
      classNames: {
        root: 'custom-button-root',
        label: 'custom-button-label'
      }
    }
  }
}

// Using a component with theme class names
<Button themeName={['Button']} />
```

The expected class names from the theme are not being applied correctly. Instead of getting the classes from `theme.components.Button.classNames`, it appears the code is trying to access them at the wrong level.

### Expected behavior

The component should properly resolve and apply the class names defined in `theme.components[componentName].classNames` for the specified selector.

### Additional context

This also affects cases where the `themeName` array might contain falsy values (like `null` or `undefined`), which should probably be filtered out before processing.

---
Repository: /testbed
