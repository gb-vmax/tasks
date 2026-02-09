# Bug Report

### Describe the bug

When swizzling components with custom descriptions, the description is not being used correctly. Instead of showing the component's actual description, it always falls back to the default description even when a valid description is provided in the component configuration.

### Reproduction

```js
// Component config with a custom description
const componentConfig = {
  description: 'My custom component description'
}

// When swizzling this component, it shows:
// "My custom component description" ❌ (expected)
// But actually shows the fallback description instead
```

### Steps to reproduce:
1. Create a theme component with a custom description in its config
2. Try to swizzle that component
3. Notice that the custom description is not displayed - the fallback description appears instead

### Expected behavior

When a component has a custom description defined in its configuration, that description should be displayed during the swizzle process. The fallback description should only be used when no description is provided (undefined or null).

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
