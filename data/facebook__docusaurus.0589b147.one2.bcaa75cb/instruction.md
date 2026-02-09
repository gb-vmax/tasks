# Bug Report

### Describe the bug

I'm experiencing an issue with markdown rendering where indented lines are not being processed correctly. The output appears to be missing content or producing garbled text when dealing with indented code blocks or nested list items.

### Reproduction

```js
const markdown = `
  - Item 1
    - Nested item
  - Item 2
`;

const result = processor.processSync(markdown);
// Output is missing or incorrect
```

When processing markdown with indented content, the resulting output doesn't match the expected formatted text. It seems like the indentation mapping function isn't being called properly or the results aren't being collected correctly.

### Expected behavior

Indented lines should be properly processed and included in the final output. Each line should be mapped through the indentation function and the results should be accumulated correctly.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
