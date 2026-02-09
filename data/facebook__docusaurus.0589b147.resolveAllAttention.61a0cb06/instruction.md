# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis/strong parsing in markdown text. When using asterisks or underscores for emphasis, the parser seems to be skipping or incorrectly processing certain attention sequences, leading to malformed output.

### Reproduction

```js
// Example markdown with nested emphasis
const markdown = `**bold _italic_ text**`;

// After parsing, the emphasis markers are not being 
// properly converted and remain as raw text or
// produce unexpected output
```

The problem appears when there are multiple attention sequences (emphasis markers) in the text. Some sequences are not being resolved correctly and remain in their raw form instead of being converted to proper emphasis nodes.

### Expected behavior

All attention sequences should be properly resolved and converted to their corresponding emphasis/strong elements. The markdown should parse correctly with nested or adjacent emphasis markers.

### Additional context

This seems to affect both asterisk-based and underscore-based emphasis. The issue is intermittent but reproducible with certain combinations of emphasis markers.

---
Repository: /testbed
