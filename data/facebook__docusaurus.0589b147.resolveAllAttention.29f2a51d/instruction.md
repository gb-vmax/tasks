# Bug Report

### Describe the bug
I'm experiencing issues with emphasis/strong emphasis parsing in markdown text. It seems like nested emphasis markers (asterisks/underscores) are not being processed correctly, leading to incorrect rendering of bold and italic text.

### Reproduction
```js
// Example markdown with nested emphasis
const markdown = `**bold *nested italic* text**`

// The output is not correctly parsing the nested emphasis
// Similar issues occur with:
const markdown2 = `*italic **nested bold** text*`
const markdown3 = `***bold and italic***`
```

When processing markdown with multiple emphasis sequences, the parser appears to skip over some markers or process them in the wrong order. This results in:
- Missing emphasis tags
- Incorrectly paired opening/closing markers
- Text that should be bold/italic being rendered as plain text

### Expected behavior
Nested emphasis markers should be correctly matched and paired, producing proper HTML output with nested `<em>` and `<strong>` tags where appropriate.

### System Info
- remark version: 15.0.1
- Browser: N/A (server-side rendering)

This seems to have started happening recently. The emphasis resolution logic might not be iterating through the attention sequences properly.

---
Repository: /testbed
