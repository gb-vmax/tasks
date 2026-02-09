# Bug Report

### Describe the bug

When trying to swizzle components, I'm getting unexpected behavior where components that should have custom configurations are falling back to default configurations instead. This seems to affect components that have explicit config entries in the swizzle config.

### Reproduction

```js
// In a Docusaurus project with a theme that has swizzle config
// Try to swizzle a component that has a custom config defined

// For example, if you have a component with this config:
const swizzleConfig = {
  components: {
    'MyComponent': {
      actions: { eject: 'safe', wrap: 'safe' },
      description: 'Custom component'
    }
  }
}

// When you try to swizzle 'MyComponent', it ignores the custom config
// and uses the fallback config instead
```

### Expected behavior

Components with explicit configurations in `swizzleConfig.components` should use their defined config, not fall back to the default `FallbackSwizzleComponentConfig`.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

This is causing issues when trying to swizzle components that should have specific safety levels or descriptions defined in the theme's swizzle configuration.

---
Repository: /testbed
