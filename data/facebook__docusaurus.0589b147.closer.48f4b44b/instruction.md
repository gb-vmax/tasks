# Bug Report

### Describe the bug

I'm experiencing a crash when processing MDX files with certain nested structures. The error occurs during the compilation phase and seems related to how tokens are being closed/exited.

### Reproduction

```js
// When compiling MDX content with nested elements
const mdx = `
# Title

<Component>
  <NestedComponent>
    Content here
  </NestedComponent>
</Component>
`

// Compilation fails with TypeError
compile(mdx)
```

### Expected behavior

The MDX content should compile successfully without errors. Nested components should be properly handled during the token closing phase.

### Error message

```
TypeError: Cannot read properties of undefined (reading 'call')
```

This happens when the compiler tries to process closing tags for nested components. It looks like something is being called before checking if it exists.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
