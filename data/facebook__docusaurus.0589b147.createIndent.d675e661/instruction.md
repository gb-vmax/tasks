# Bug Report

### Describe the bug

I'm experiencing an issue with indentation in MDX code blocks. When rendering nested MDX elements, the indentation appears to be off by one level - there's an extra indent being added that shouldn't be there.

### Reproduction

```js
const mdx = `
<Component>
  <NestedComponent>
    Content here
  </NestedComponent>
</Component>
`

// When parsed and stringified, the output has incorrect indentation
// Expected: proper nesting with correct indent levels
// Actual: extra indentation added to nested elements
```

The indentation for nested components is deeper than it should be, making the output look incorrectly formatted.

### Expected behavior

Nested MDX elements should maintain proper indentation levels without adding extra indents. Each nesting level should increment the indentation by exactly one level, not more.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
