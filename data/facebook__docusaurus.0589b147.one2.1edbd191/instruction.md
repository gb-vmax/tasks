# Bug Report

### Describe the bug

I'm seeing duplicate content being generated when using markdown formatting with indented lines. It looks like the indentation mapping function is being called twice, which causes the mapped content to appear duplicated in the output.

### Reproduction

```js
const content = `
line 1
line 2
line 3
`;

// When processing with indentation
const result = processMarkdown(content);
// Output contains duplicated mapped content
```

### Expected behavior

Each line should only be processed once through the indentation mapper. The output should contain the original content with proper indentation applied, not duplicated text.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
