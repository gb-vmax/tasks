# Bug Report

### Describe the bug

I'm encountering an issue with footnote definitions in the markdown parser. When parsing GFM (GitHub Flavored Markdown) footnotes, the footnote definition structure appears to be malformed, causing problems when trying to access or iterate over the children of a footnote.

### Reproduction

```js
// Parse markdown with a footnote definition
const markdown = `
Here's a sentence with a footnote[^1].

[^1]: This is the footnote content.
`;

const ast = parseMarkdown(markdown);
const footnoteNode = findFootnoteDefinition(ast);

// Trying to access children throws an error
console.log(footnoteNode.children); // Expected: array, Got: undefined

// Trying to iterate over children fails
footnoteNode.children.forEach(child => {
  // This crashes because children is undefined
  console.log(child);
});
```

### Expected behavior

The `footnoteDefinition` node should have a `children` property that is an empty array (or array with content), not `undefined`. This breaks any code that tries to iterate over or process the children of footnote definitions.

Also, the `identifier` should be an empty string (or the actual identifier), not `null`, which can cause type errors when string operations are expected.

### Additional context

This seems to affect any markdown content that includes footnote definitions. The parser creates nodes with invalid structure that don't match the expected AST format.

---
Repository: /testbed
