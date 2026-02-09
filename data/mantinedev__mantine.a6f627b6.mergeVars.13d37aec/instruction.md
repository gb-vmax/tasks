# Bug Report

### Describe the bug

I'm experiencing an issue with CSS variable merging when using multiple style overrides. When I apply styles with CSS variables at different levels (e.g., component props and theme overrides), the variables from earlier sources are overriding later ones instead of the other way around.

### Reproduction

```tsx
const theme = {
  components: {
    Button: {
      vars: {
        root: {
          '--button-color': 'red'
        }
      }
    }
  }
}

// Later in component
<Button vars={{ root: { '--button-color': 'blue' } }} />
```

Expected: The button color should be blue (from the component prop)
Actual: The button color is red (from the theme)

### Steps to reproduce
1. Define CSS variables in theme component configuration
2. Try to override those variables via component props
3. The theme variables take precedence instead of the prop variables

This seems like the merge order might be reversed somewhere. The more specific/local variables should override the more general/global ones.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
