# Bug Report

### Describe the bug

Template literals are not being parsed correctly, causing the parser to fail when encountering backtick-delimited strings or template expressions with `${}` interpolation.

### Reproduction

```js
const code = `
const greeting = \`Hello, \${name}!\`;
const multiline = \`
  Line 1
  Line 2
\`;
`;

// Parser fails to process template literals
parse(code);
```

### Expected behavior

Template literals should be properly tokenized and parsed, including:
- Backtick-delimited strings
- Expression interpolation with `${}`
- Multi-line templates
- Escaped characters within templates

### Additional context

This appears to affect any code containing template literal syntax. The parser seems unable to recognize or process the template token structure, which is breaking MDX parsing for files that include JavaScript template strings.

---
Repository: /testbed
