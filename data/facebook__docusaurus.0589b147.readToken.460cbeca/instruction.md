# Bug Report

### Describe the bug

I'm encountering an issue where valid JavaScript identifiers are not being parsed correctly in MDX files. It seems like the parser is failing to recognize standard identifier characters, causing syntax errors on what should be valid code.

### Reproduction

```jsx
// This MDX code should work but throws a parsing error
export const MyComponent = () => {
  const validIdentifier = 'test';
  return <div>{validIdentifier}</div>;
};
```

When trying to parse MDX content with normal JavaScript variable names, the parser rejects them as invalid tokens. This affects:
- Regular variable declarations
- Function names
- Component names
- Any standard JavaScript identifier

### Expected behavior

The parser should correctly recognize valid JavaScript identifiers (letters, `$`, `_`, etc.) and allow them to be used normally in MDX content. Standard JavaScript/JSX code should parse without errors.

### System Info
- remark-mdx version: 3.0.0

This appears to have started recently, possibly after an update. Previously working MDX files are now failing to parse.

---
Repository: /testbed
