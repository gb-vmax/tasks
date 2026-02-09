# Bug Report

### Describe the bug

I'm experiencing an issue with parsing MDX documents where content is not being processed correctly. It seems like the parser is failing to recognize valid document structures and treating them as errors instead.

### Reproduction

```js
const mdx = `
# Hello World

This is a simple MDX document with a heading and paragraph.
`;

// When parsing this MDX content, it fails unexpectedly
const result = compile(mdx);
```

The parser appears to be rejecting valid document content that should be accepted. This is affecting basic MDX documents with standard markdown elements.

### Expected behavior

Valid MDX/markdown content should be parsed successfully without errors. Simple documents with headings and paragraphs should work as expected.

### Additional context

This might be related to how the document tokenizer is handling the success/error callbacks. The behavior changed recently and now even basic documents are failing to parse correctly.

---
Repository: /testbed
