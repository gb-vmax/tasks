# Bug Report

### Describe the bug

Strikethrough syntax in GFM (GitHub Flavored Markdown) is not being parsed correctly. When using double tildes (`~~`) to wrap text, the strikethrough formatting is not being applied as expected.

### Reproduction

```js
const markdown = '~~strikethrough text~~'
// Expected: text should be wrapped in strikethrough tags
// Actual: strikethrough is not being recognized/parsed
```

Also happens with inline strikethrough:
```
This is ~~some text~~ with strikethrough.
```

The parser seems to be rejecting valid strikethrough sequences. This worked fine in previous versions but appears to be broken now.

### Expected behavior

Text wrapped in double tildes should be parsed as strikethrough formatting according to GFM spec. The markdown `~~text~~` should result in properly formatted strikethrough output.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
