# Bug Report

### Describe the bug

Footnote definitions are being incorrectly parsed as footnote references. When processing markdown with footnote definitions (the `[^1]: ...` syntax), the parser creates nodes with type `footnoteReference` instead of `footnoteDefinition`.

### Reproduction

```js
const markdown = `
Some text with a footnote[^1].

[^1]: This is the footnote definition.
`;

// Parse the markdown
const ast = parseMarkdown(markdown);

// The footnote definition node has the wrong type
console.log(ast.children.find(node => node.identifier === '1'));
// Expected: { type: 'footnoteDefinition', ... }
// Actual: { type: 'footnoteReference', ... }
```

### Expected behavior

When parsing footnote definitions in markdown (e.g., `[^1]: footnote text`), the AST should contain nodes with `type: "footnoteDefinition"`. Currently, these are being created with `type: "footnoteReference"` which is incorrect - footnote references are the inline citations like `[^1]`, while footnote definitions are the actual footnote content.

This breaks any downstream processing that relies on distinguishing between footnote references and their definitions.

---
Repository: /testbed
