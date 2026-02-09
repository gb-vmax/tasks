# Bug Report

### Describe the bug

I'm experiencing an issue where markdown content with multiple child nodes is not being processed correctly. It seems like the first element in a sequence is being skipped or lost during conversion.

### Reproduction

When processing markdown with multiple elements (like a list with multiple items, or multiple paragraphs), the first element disappears from the output:

```js
// Example with a list
const markdown = `
- First item
- Second item
- Third item
`;

// After processing, output only contains:
// "Second item\nThird item"
// The first item is missing
```

Same thing happens with other node types that have multiple children - the first child element is consistently dropped.

### Expected behavior

All elements should be preserved in the output. The first item/element should not be skipped during processing.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
