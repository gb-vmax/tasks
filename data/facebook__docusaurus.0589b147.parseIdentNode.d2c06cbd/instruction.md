# Bug Report

### Describe the bug

I'm encountering an issue with identifier parsing in MDX where certain identifiers are not being parsed correctly. It seems like the parser is using the wrong property to get the identifier name, which causes unexpected behavior when processing JavaScript/JSX code.

### Reproduction

```jsx
// When parsing identifiers, the name extraction fails
const Component = () => {
  const myVar = "test";
  return <div>{myVar}</div>;
}
```

The parser appears to be extracting identifier names incorrectly, leading to malformed AST nodes. This affects variable references and other identifiers in the code.

### Expected behavior

Identifiers should be parsed correctly with their proper names extracted from the token value. The parser should accurately capture variable names, function names, and other identifiers as they appear in the source code.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
