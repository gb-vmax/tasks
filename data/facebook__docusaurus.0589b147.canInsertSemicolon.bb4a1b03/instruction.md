# Bug Report

### Describe the bug

I'm experiencing issues with automatic semicolon insertion (ASI) in MDX parsing. It seems like semicolons are not being inserted correctly in certain cases, causing parsing errors where they shouldn't occur.

### Reproduction

```jsx
// This should parse correctly but throws an error
export const config = {
  runtime: 'edge'
}

function MyComponent() {
  return <div>Hello</div>
}
```

The parser fails when it should automatically insert a semicolon after the closing brace of the object. This works fine in regular JavaScript/JSX but breaks in MDX files.

### Expected behavior

The parser should correctly identify positions where automatic semicolon insertion is allowed (after `}`, at EOF, or after line breaks) and handle the code without errors.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
