# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where certain destructuring patterns are being incorrectly flagged as errors. It seems like the parser is treating valid destructuring syntax as invalid, causing parsing to fail unexpectedly.

### Reproduction

```jsx
const Component = () => {
  const { a, b } = props;
  return <div>{a} {b}</div>;
};
```

When this code is parsed, it throws an error even though the destructuring pattern is valid JavaScript/JSX syntax. This appears to affect various destructuring scenarios including object destructuring in function parameters and variable declarations.

### Expected behavior

Valid destructuring patterns should parse successfully without throwing errors. The parser should correctly identify and handle legitimate destructuring syntax in MDX files.

### Additional context

This seems to have started happening recently. Previously, the same MDX files with destructuring patterns were parsing without issues. The problem affects both simple and complex destructuring patterns.

---
Repository: /testbed
