# Bug Report

### Describe the bug

When using the swizzle command, component descriptions are not being displayed correctly. All components are showing the same fallback description instead of their actual descriptions defined in the theme config.

### Reproduction

```bash
# Try to swizzle any component with a custom description
npm run swizzle @docusaurus/theme-classic ComponentName
```

Expected: Should show the component's specific description from the theme configuration
Actual: Always shows the generic fallback description regardless of what's configured

### Steps to reproduce

1. Set up a Docusaurus project with a theme that has components with custom descriptions
2. Run the swizzle command for a component that has a description defined
3. Observe that the description shown is always the fallback description, not the actual component description

This seems to affect all themed components - none of them are showing their proper descriptions anymore.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
