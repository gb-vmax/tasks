# Bug Report

### Describe the bug

I'm encountering an issue with inline code rendering in MDX. After a recent update, inline code blocks are not being processed correctly and appear to have a different structure than expected.

### Reproduction

```js
const mdxContent = `
This is a paragraph with \`inline code\` in it.
`;

// Process the MDX content
const result = compile(mdxContent);
```

When I inspect the AST output, the inline code nodes have an unexpected structure. Instead of the standard `inlineCode` type, they now have a different type and nested structure that breaks downstream processing.

### Expected behavior

Inline code should be represented as a simple `inlineCode` node type in the AST, consistent with previous versions. The current structure causes issues with custom remark/rehype plugins that expect the standard node format.

### Additional context

This seems to have started happening recently. Not sure if this was an intentional change or a regression, but it's breaking compatibility with existing MDX tooling.

---
Repository: /testbed
