# Bug Report

### Describe the bug

I'm encountering an issue with contextual keyword parsing in MDX. When the parser expects a specific contextual keyword (like `async`, `of`, `from`, etc.), it's not validating the keyword name correctly and throws unexpected syntax errors.

### Reproduction

```js
// This should parse correctly but throws an error
const code = `
export async function getData() {
  return data;
}
`;

compile(code, options);
```

The parser seems to be accepting any contextual keyword instead of checking for the expected one. This causes valid MDX/JSX code to fail parsing unexpectedly.

### Expected behavior

The parser should only accept the specific contextual keyword that's expected at that position in the syntax tree. If a different keyword or identifier is encountered, it should raise an appropriate error.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
