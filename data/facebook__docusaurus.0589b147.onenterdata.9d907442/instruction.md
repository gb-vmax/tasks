# Bug Report

### Describe the bug

I'm experiencing a crash when parsing MDX content with text nodes. The parser throws an error when trying to access properties on `undefined` or `null` values during the data token processing phase.

### Reproduction

```js
// Any MDX content with text seems to trigger this
const mdx = `
# Hello World

This is some text content.
`;

// Parsing fails with cannot read property 'type' of undefined
compile(mdx);
```

### Expected behavior

The MDX content should parse successfully and text nodes should be created and added to the AST without errors.

### Additional context

This seems to happen specifically when the parser enters data tokens and tries to work with text nodes. The error appears to be related to checking the type of the tail node before it's properly validated.

---
Repository: /testbed
