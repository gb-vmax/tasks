# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in markdown parsing. When using backticks for inline code (e.g., `` `code` ``), the parsed output is incorrect. The inline code elements are not being created with the proper type and value.

### Reproduction

```js
const markdown = 'This is `inline code` in text';
const parsed = parseMarkdown(markdown);

// Expected: { type: "inlineCode", value: "inline code" }
// Actual: { type: "inline", value: undefined }
```

When I parse markdown containing inline code blocks, the resulting AST nodes have:
- Wrong type: `"inline"` instead of `"inlineCode"`
- Missing value: `undefined` instead of the actual code string

### Expected behavior

Inline code elements should be parsed as `inlineCode` type nodes with the code content properly preserved in the `value` field.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
