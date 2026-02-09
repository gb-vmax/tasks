# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis markers in markdown rendering. When processing emphasis/italic text, the output appears to be missing the emphasis markers entirely, resulting in plain text instead of properly formatted emphasis.

### Reproduction

```js
const markdown = '*italic text*';
const result = remark().stringify(parse(markdown));
// Expected: '*italic text*'
// Actual: 'italic text' (no emphasis markers)
```

The emphasis markers are being stripped out during the stringify process. This affects both asterisk (`*`) and underscore (`_`) style emphasis.

### Expected behavior

The emphasis markers should be preserved in the output when stringifying markdown AST nodes. The text should remain wrapped in the appropriate emphasis characters.

### Additional context

This seems to affect the peek function for emphasis nodes. The markers are not being returned correctly, which causes the stringification to fail to add the proper delimiters around emphasized text.

---
Repository: /testbed
