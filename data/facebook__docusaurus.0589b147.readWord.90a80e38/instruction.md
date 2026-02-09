# Bug Report

### Describe the bug
When parsing MDX code, keywords are not being recognized correctly. Instead of identifying reserved keywords like `if`, `else`, `function`, etc., the parser treats them as regular identifiers. This causes syntax highlighting and code analysis to fail for valid JavaScript/JSX code blocks.

### Reproduction
```js
// This MDX content should recognize 'function' as a keyword
const mdxContent = `
function MyComponent() {
  if (true) {
    return <div>Hello</div>
  }
}
`

// Parse the MDX
// Expected: 'function' and 'if' are recognized as keywords
// Actual: They are treated as regular names/identifiers
```

### Expected behavior
Keywords like `function`, `if`, `else`, `return`, etc. should be properly identified and tokenized as keywords rather than generic name tokens.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
