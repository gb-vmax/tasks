# Bug Report

### Describe the bug

I'm experiencing a stack overflow error when parsing MDX content with JSX tags. The parser seems to get stuck in an infinite loop and eventually crashes with a "Maximum call stack size exceeded" error.

### Reproduction

```js
const mdx = `
# Hello

<MyComponent>
  Some content here
</MyComponent>
`;

// Parsing this causes a stack overflow
const result = parseMdx(mdx);
```

The error occurs when the parser tries to process JSX tags in the MDX content. It seems like something is recursively calling itself without a proper base case.

### Expected behavior

The MDX content should parse successfully without throwing a stack overflow error. The JSX tags should be properly converted to the AST representation.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This is blocking our documentation build process. Any help would be appreciated!

---
Repository: /testbed
