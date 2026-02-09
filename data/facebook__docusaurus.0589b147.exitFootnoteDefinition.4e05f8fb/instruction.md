# Bug Report

### Describe the bug

I'm encountering an issue with footnote definitions in markdown parsing. After processing a document with footnotes, the footnote definitions are being incorrectly transformed into footnote references instead of remaining as definitions.

### Reproduction

```js
const markdown = `
Here is some text with a footnote[^1].

[^1]: This is the footnote definition.
`;

// Parse the markdown
const result = parseMarkdown(markdown);

// The footnote definition node has type 'footnoteReference' instead of 'footnoteDefinition'
console.log(result.children); // Shows incorrect node type
```

### Expected behavior

Footnote definitions should maintain their `footnoteDefinition` type throughout the parsing process. The AST should correctly distinguish between:
- `footnoteReference` - the inline reference like `[^1]`
- `footnoteDefinition` - the actual definition like `[^1]: text`

Currently, the definition is being converted to a reference type, which breaks the semantic structure of the document.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
