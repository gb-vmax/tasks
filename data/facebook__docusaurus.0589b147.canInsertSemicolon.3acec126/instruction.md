# Bug Report

### Describe the bug

I'm experiencing an issue with automatic semicolon insertion (ASI) in MDX parsing. It seems like the parser is incorrectly determining when semicolons can be inserted, causing valid MDX code to fail parsing or invalid code to be accepted.

### Reproduction

```jsx
// This should parse correctly but doesn't
export const config = {
  title: 'Test'
}

function Component() {
  return <div>Hello</div>
}
```

The parser appears to be checking for semicolon insertion opportunities incorrectly. In some cases where a semicolon should be auto-inserted (like after a closing brace), it's not being detected properly.

### Expected behavior

The MDX parser should correctly identify positions where automatic semicolon insertion is allowed according to JavaScript ASI rules - specifically at EOF, before closing braces, or when there's a line break between tokens.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
