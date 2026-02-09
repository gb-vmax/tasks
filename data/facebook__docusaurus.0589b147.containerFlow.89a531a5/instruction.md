# Bug Report

### Describe the bug

I'm encountering an issue with markdown serialization where the output seems to be off by one position. When converting markdown AST nodes back to text, the resulting markdown has incorrect line breaks or spacing between elements, particularly when dealing with flow content like lists and paragraphs.

### Reproduction

```js
const markdown = `
1. First item
2. Second item

Paragraph after list

3. Another list item
`;

const tree = parseMarkdown(markdown);
const output = serializeToMarkdown(tree);

// The output has incorrect spacing/positioning
console.log(output);
```

### Expected behavior

The serialized markdown should maintain the same structure and spacing as the original input. List items and paragraphs should be properly separated with the correct number of line breaks.

### Additional context

This seems to affect how the position tracking works internally when processing flow containers. The issue becomes more noticeable with complex nested structures or when mixing different types of block elements.

---
Repository: /testbed
