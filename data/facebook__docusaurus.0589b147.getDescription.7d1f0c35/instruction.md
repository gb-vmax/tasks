# Bug Report

### Describe the bug

When using the swizzle command to get component descriptions, the wrong component ID is being used internally. The function is receiving a `component` parameter but then references a different variable `componentId` that doesn't exist in that scope, which causes the description lookup to fail.

### Reproduction

```bash
# Try to swizzle a component and view its description
npx docusaurus swizzle [theme-name] [component-name]
```

The component description will not be retrieved correctly because the function is looking up the wrong variable.

### Expected behavior

The `getDescription` function should use the `component` parameter that is passed to it, not an undefined `componentId` variable. Component descriptions should be displayed correctly when swizzling components.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
