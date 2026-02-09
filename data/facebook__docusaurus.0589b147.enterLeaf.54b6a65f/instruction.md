# Bug Report

### Describe the bug

I'm encountering an issue with leaf directives in markdown processing. When parsing markdown content that contains leaf directives (like `::directive`), the parser appears to be failing or producing incorrect output.

### Reproduction

```js
const markdown = `
Some text before

::my-leaf-directive[content here]

Some text after
`;

// Process the markdown with remark-directive
const result = processor.parse(markdown);
```

When processing markdown with leaf directives, the directive nodes are not being created correctly in the AST. The context seems to be lost during parsing, which prevents the directive from being properly recognized and transformed.

### Expected behavior

Leaf directives should be parsed correctly and appear as proper nodes in the syntax tree with all their properties intact. The directive should maintain its context and be accessible for further processing.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
