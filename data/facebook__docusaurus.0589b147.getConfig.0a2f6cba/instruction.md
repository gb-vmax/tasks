# Bug Report

### Describe the bug

When swizzling components that have explicit configurations in the swizzle config, the component's configuration is being ignored and the fallback config is used instead. This causes components to behave as if they have no specific swizzle settings, even when they're properly defined in the theme's swizzle configuration.

### Reproduction

1. Define a component with a specific swizzle config (e.g., marking it as safe/unsafe or setting custom actions)
2. Try to swizzle that component
3. The component is treated as if it has the default fallback configuration instead of its actual defined config

For example, if a component is configured as:
```js
components: {
  'MyComponent': {
    actions: {
      eject: 'safe',
      wrap: 'unsafe'
    },
    description: 'Custom component'
  }
}
```

The swizzle command will ignore these settings and use the fallback configuration instead.

### Expected behavior

Components with explicit swizzle configurations should use their defined settings, not fall back to the default configuration. The component config should be properly returned when it exists in the swizzle config.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
