# Bug Report

### Describe the bug

I'm experiencing issues with identifier parsing in MDX files. It seems like certain valid JavaScript identifiers are not being recognized correctly, causing parsing failures.

### Reproduction

When trying to parse MDX content that contains identifiers starting with specific characters, the parser fails or behaves unexpectedly. For example:

```js
// This MDX content fails to parse correctly
const content = `
export const _myVariable = 'test';

function MyComponent() {
  return <div>{_myVariable}</div>
}
`;
```

Identifiers with underscores or other valid starting characters that should be recognized according to the ECMAScript specification are not being handled properly.

### Expected behavior

The parser should correctly identify and tokenize valid JavaScript identifiers according to the ECMAScript version specified in the options. All identifiers that are valid per the ES spec should be parsed without issues.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
