# Bug Report

### Describe the bug

I'm experiencing an issue with markdown formatting where indented lines are not being processed correctly. It seems like the indentation mapping function is receiving arguments in the wrong order, causing the output to be malformed.

### Reproduction

```js
const markdown = `
  - Item 1
    - Nested item
  - Item 2
`;

// Process markdown with indentation
const result = processMarkdown(markdown);
console.log(result);
```

When processing markdown content with nested indentation (like lists or code blocks), the indentation level is not being applied correctly. The output shows incorrect formatting where the indentation appears to be calculated based on wrong parameters.

### Expected behavior

The markdown processor should correctly apply indentation to nested content, preserving the hierarchical structure. The indentation mapping function should receive the correct line content and index values to properly format the output.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
