# Bug Report

### Describe the bug

I'm experiencing an issue with parsing variable declarations in MDX files. It seems like the parser is skipping tokens or consuming extra tokens when processing `var`, `let`, or `const` statements, causing syntax errors or unexpected behavior.

### Reproduction

```jsx
const MyComponent = () => {
  const value = 42;
  return <div>{value}</div>;
}
```

When trying to parse this MDX content, the parser fails to correctly handle the variable declaration. The issue appears to be related to how the parser processes the tokens in variable statements.

### Expected behavior

Variable declarations should be parsed correctly without any token skipping issues. The parser should properly handle:
- `const` declarations
- `let` declarations  
- `var` declarations

All of these should work seamlessly in MDX content.

### Additional context

This seems to have started happening recently. The parser might be consuming tokens twice or in the wrong order when processing variable statements, which breaks the parsing flow.

---
Repository: /testbed
