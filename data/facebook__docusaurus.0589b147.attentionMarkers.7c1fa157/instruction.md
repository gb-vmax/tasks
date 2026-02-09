# Bug Report

### Describe the bug

I'm experiencing an issue where emphasis markers (like `*` and `_`) are not being parsed correctly in markdown. When I try to use bold or italic formatting, the text is rendered as plain text instead of being styled.

### Reproduction

```js
const markdown = '*italic text* and **bold text**';
const result = remark().processSync(markdown);
console.log(result);
// Expected: Parsed AST with emphasis/strong nodes
// Actual: Plain text nodes without any emphasis formatting
```

Another example:
```js
const text = '_underscored text_ should be italic';
// The underscores are treated as literal characters instead of emphasis markers
```

### Expected behavior

Markdown emphasis syntax using `*` and `_` should be properly recognized and converted to emphasis/strong nodes in the AST. Both single asterisks/underscores for italic and double for bold should work as standard markdown.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have broken recently, as the same markdown was working fine before. The emphasis markers are just being ignored completely.

---
Repository: /testbed
