# Bug Report

### Describe the bug

When trying to swizzle theme components, the swizzle configuration from the theme's `swizzle.js` file is being ignored. All components are falling back to the default configuration instead of respecting the specific configuration defined by the theme.

### Reproduction

1. Create a Docusaurus theme with a `swizzle.js` configuration file that defines custom swizzle actions for components
2. Try to swizzle a component that has specific configuration (e.g., a component marked as `safe` for wrapping)
3. The component behaves as if no custom configuration exists

For example, if a theme defines:
```js
// swizzle.js
module.exports = {
  components: {
    'MyComponent': {
      actions: {
        wrap: 'safe',
        eject: 'unsafe'
      }
    }
  }
}
```

The component will not respect these settings and will use the fallback configuration instead.

### Expected behavior

Components should use their specific swizzle configuration as defined in the theme's `swizzle.js` file. The fallback configuration should only be used when no specific configuration is provided for a component.

### Additional context

This affects the ordering of components in the swizzle prompt as well, since the sorting logic relies on the component configurations being read correctly.

---
Repository: /testbed
