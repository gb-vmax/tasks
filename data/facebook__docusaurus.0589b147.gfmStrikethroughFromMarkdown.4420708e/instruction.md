# Bug Report

### Describe the bug
When using strikethrough syntax in markdown (e.g., `~~text~~`), the parser seems to be treating the `delete` token incorrectly. The `canContainEols` configuration is using an array format instead of the expected object format, which causes issues with how nested content inside strikethrough blocks is handled.

### Reproduction
```js
// Parse markdown with strikethrough containing line breaks
const markdown = `~~This is
a multiline
strikethrough~~`

// The parser fails to properly handle the nested content
// because canContainEols is configured as an array instead of an object
```

### Expected behavior
Strikethrough blocks should correctly handle content that spans multiple lines. The `canContainEols` configuration should be an object (like `{ delete: true }`) to properly indicate that delete nodes can contain end-of-line characters.

Additionally, both `strikethrough` and `delete` tokens should have proper enter/exit handlers registered since they represent the same semantic element in the markdown tree.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
