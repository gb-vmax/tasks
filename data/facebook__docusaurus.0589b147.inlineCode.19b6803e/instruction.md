# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in markdown. When I try to use inline code with backticks, the output is not being formatted correctly. It seems like the logic for determining when to add padding spaces around the code content is inverted.

### Reproduction

```js
// Example 1: Code with non-whitespace content
const markdown = '`hello`';
// Expected: `hello`
// Actual: ` hello ` (incorrectly adds spaces)

// Example 2: Code that should have padding
const markdown2 = '` `';
// Expected: `  ` (with padding spaces)
// Actual: ` ` (no padding added)
```

The issue appears to be affecting how inline code blocks are serialized. Content that shouldn't have padding is getting extra spaces, while content that needs padding to disambiguate from delimiters is not getting it.

### Expected behavior

Inline code should only have padding spaces added when:
1. The content starts or ends with whitespace AND contains non-whitespace characters
2. OR when the content starts/ends with backticks

Regular inline code without these edge cases should render without extra padding.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
