# Bug Report

### Describe the bug

I'm encountering an issue with HTML flow tokenization in the markdown parser. When processing HTML blocks that have trailing whitespace after closing tags, the parser fails to properly recognize the end of the HTML block and continues parsing incorrectly.

### Reproduction

```js
const markdown = `
<div>
  content
</div>   
More text here
`

// The parser fails to properly handle the whitespace after </div>
// and doesn't correctly identify where the HTML block ends
```

### Expected behavior

The parser should correctly handle HTML blocks even when there's trailing whitespace after the closing tag. The HTML block should be properly closed and subsequent content should be parsed as regular markdown text.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
