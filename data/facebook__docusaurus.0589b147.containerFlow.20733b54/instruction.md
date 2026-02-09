# Bug Report

### Describe the bug

I'm experiencing an issue with markdown rendering where content appears to be duplicated or processed incorrectly. When converting certain markdown structures to output, there seems to be an extra iteration happening that causes unexpected behavior.

### Reproduction

```js
const markdown = `
# Heading

First paragraph.

Second paragraph.

Third paragraph.
`;

const result = remark().stringify(parse(markdown));
// Output contains duplicate content or extra blank sections
```

### Expected behavior

The markdown should be processed exactly once for each element, with proper spacing between flow content elements. No duplication or extra iterations should occur.

### Additional context

This seems to affect flow containers (paragraphs, headings, lists, etc.) specifically. The issue appears when there are multiple consecutive elements in the document tree.

---
Repository: /testbed
