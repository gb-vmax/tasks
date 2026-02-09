# Bug Report

### Describe the bug

Components are failing the static classes validation check. It seems like the classes object validation is incorrectly rejecting valid class objects.

### Reproduction

When creating a component with a static classes object:

```tsx
const MyComponent = {
  classes: {
    root: 'my-component-root',
    inner: 'my-component-inner'
  }
}
```

The classes validation fails even though the classes object is properly defined and not null.

### Expected behavior

Components with valid static classes objects (non-null objects that aren't arrays) should pass the validation check. The classes object should be recognized as a valid object structure.

### System Info
- Mantine version: Latest
- Testing framework: Jest/React Testing Library

---
Repository: /testbed
