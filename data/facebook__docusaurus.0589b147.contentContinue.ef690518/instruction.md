# Bug Report

### Describe the bug

I'm encountering an issue where markdown content parsing appears to be broken. When processing markdown documents with multi-line content blocks, the parser seems to fail or hang instead of properly tokenizing the content.

### Reproduction

```js
const markdown = `
This is a paragraph
that spans multiple lines
and should be parsed correctly.

Another paragraph here.
`;

// Parse the markdown
const result = parse(markdown);
// Parser fails to process continuation of content chunks
```

### Expected behavior

The parser should correctly tokenize and process multi-line content blocks, allowing content to continue across multiple lines within the same block. Each chunk of content should be properly linked to the previous chunk for continuous parsing.

### Additional context

This seems to affect any markdown content that spans multiple lines within a single block. The parsing either stops prematurely or doesn't handle the continuation of content chunks properly.

---
Repository: /testbed
