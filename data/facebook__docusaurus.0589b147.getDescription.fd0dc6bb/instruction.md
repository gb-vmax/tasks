# Bug Report

### Describe the bug

When using the swizzle command, components with `description: null` in their configuration are not displaying the fallback description. Instead of showing the default fallback text, they appear to be showing `null` or an empty description.

### Reproduction

```js
// In theme component config
const componentConfig = {
  description: null,
  // other config...
}

// When swizzling, the description should fall back to FallbackSwizzleComponentDescription
// but it doesn't work as expected
```

Steps to reproduce:
1. Configure a swizzleable component with `description: null`
2. Run the swizzle command for that component
3. The component description doesn't show the fallback value

### Expected behavior

When a component's description is explicitly set to `null`, it should fall back to `FallbackSwizzleComponentDescription` just like when the description is `undefined` or missing.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
