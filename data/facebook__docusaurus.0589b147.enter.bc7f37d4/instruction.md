# Bug Report

### Describe the bug

When converting markdown AST to markdown string using `toMarkdown()`, the output contains duplicate content for nested structures. It appears that nested elements are being rendered twice, causing malformed markdown output.

### Reproduction

```js
import {toMarkdown} from 'mdast-util-to-markdown'

const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        {
          type: 'strong',
          children: [
            {type: 'text', value: 'Hello'}
          ]
        }
      ]
    }
  ]
}

const result = toMarkdown(tree)
console.log(result)
// Expected: **Hello**
// Actual: ****Hello****
```

The nested `strong` element gets doubled in the output. This happens with other nested structures as well (emphasis, links, etc.).

### Expected behavior

The markdown output should correctly represent the AST structure without duplicating nested elements. Each node should be entered and exited exactly once during traversal.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
