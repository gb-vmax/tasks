# Bug Report

### Describe the bug

I'm encountering an issue with semicolon parsing in MDX code blocks. It seems like the parser is now throwing unexpected token errors in cases where semicolons should be optional or automatically inserted.

### Reproduction

```jsx
// This MDX code now fails to parse
export const Component = () => {
  return <div>Hello</div>
}

// The parser throws an error even though the semicolon should be auto-inserted
const value = 42
console.log(value)
```

The parser is rejecting valid JavaScript/JSX code that relies on automatic semicolon insertion (ASI). This worked fine in previous versions.

### Expected behavior

The parser should handle cases where semicolons are omitted and can be automatically inserted according to JavaScript ASI rules. Code that doesn't explicitly include semicolons should still parse correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
