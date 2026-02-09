# Bug Report

### Describe the bug

Strikethrough text rendering is broken in markdown parsing. When using the `~~text~~` syntax for strikethrough, the output is completely incorrect - the text appears with wrong formatting or in unexpected positions.

### Reproduction

```js
const markdown = '~~strikethrough text~~';
// Parse the markdown with GFM strikethrough enabled
const result = parseMarkdown(markdown);
// The output structure is malformed
```

Also happens with nested content:
```markdown
~~This is **bold** inside strikethrough~~
```

The parser seems to be handling the enter/exit events incorrectly, causing the AST structure to be inverted or malformed.

### Expected behavior

Strikethrough syntax should properly parse and render as deleted/strikethrough text. The AST should have the correct structure with proper nesting of child nodes.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
