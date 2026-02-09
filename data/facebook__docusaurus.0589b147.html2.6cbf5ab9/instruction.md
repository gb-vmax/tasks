# Bug Report

### Describe the bug

After a recent update, HTML nodes in markdown are not being parsed correctly. The parser seems to be generating nodes with an incorrect type, causing downstream processing to fail.

### Reproduction

```js
import {remark} from 'remark'

const markdown = `
Some text with <div>HTML content</div> in it.
`

const result = remark().parse(markdown)

// Inspect the AST nodes
console.log(result.children)
// Expected: nodes with type "html"
// Actual: nodes with type "htm" (truncated)
```

When parsing markdown containing inline HTML, the resulting AST contains nodes with type `"htm"` instead of `"html"`. This breaks any plugins or processors that expect the standard node type.

### Expected behavior

HTML nodes in the AST should have `type: "html"` as per the mdast specification. The node structure should match the expected format without extra properties like `children: null`.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
