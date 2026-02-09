# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where `this` keyword behavior seems incorrect in certain scope contexts. The parser appears to be skipping the current scope when determining the `this` scope, which leads to unexpected binding behavior.

### Reproduction

```js
// Example MDX content that triggers the issue
const mdxContent = `
export function MyComponent() {
  return <div>{this.props.value}</div>
}
`;

// When parsing this, the `this` context is resolved incorrectly
// It seems to skip the immediate function scope and look at parent scopes instead
```

### Expected behavior

The parser should correctly identify the current function scope as the `this` scope when appropriate. The `this` keyword should bind to the nearest non-arrow function scope, starting from the current scope position.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
