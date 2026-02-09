# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where content is being processed incorrectly, resulting in an extra `undefined` value being appended to the output. When processing markdown with multiple elements, the parser seems to be iterating one time too many through the collection.

### Reproduction

```js
const markdown = `
# Heading
Paragraph text
- List item
`;

const result = parseMarkdown(markdown);
// Expected: "Heading\nParagraph text\nList item"
// Actual: "Heading\nParagraph text\nList item\nundefined"
```

The parsed output includes an unexpected `undefined` at the end when converting markdown nodes to plain text.

### Expected behavior

The markdown parser should only process the actual elements in the collection and not attempt to access elements beyond the array bounds. The output should be clean without any trailing `undefined` values.

### Additional context

This appears to be related to how the parser iterates through child nodes. The issue manifests when there are multiple markdown elements that need to be processed sequentially.

---
Repository: /testbed
