# Bug Report

### Describe the bug

When processing markdown content with admonition titles that have no indentation, the output incorrectly includes `undefined` in the resulting string. This happens when the `indentation` capture group is not matched in the regex.

### Reproduction

```js
const content = `:::note My Title
Some content
:::`;

const result = admonitionTitleToDirectiveLabel(content, ['note', 'tip', 'warning']);

// Expected: ":::note[My Title]\nSome content\n:::"
// Actual: "undefined:::note[My Title]\nSome content\n:::"
```

The issue occurs when there's no indentation before the admonition directive. The regex capture group for `indentation` is optional, so when it doesn't match, it returns `undefined`, which gets inserted into the output string instead of an empty string.

### Expected behavior

When there's no indentation, the output should not include the string "undefined". The function should handle optional capture groups properly by treating missing matches as empty strings.

### System Info
- Package: @docusaurus/utils
- Version: latest

---
Repository: /testbed
