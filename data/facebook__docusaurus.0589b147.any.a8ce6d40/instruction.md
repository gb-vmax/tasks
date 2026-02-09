# Bug Report

### Describe the bug

I'm experiencing an issue where certain node type checks in remark are not working correctly. When using composite matchers (like checking if a node matches any of several types), the matching logic seems to be off and returns unexpected results.

### Reproduction

```js
import {remark} from 'remark'
import {visit} from 'unist-util-visit'

const markdown = `
# Heading

Some text
`

const tree = remark.parse(markdown)

// Try to match nodes using composite checks
visit(tree, (node) => {
  // Check for multiple node types
  if (isHeadingOrParagraph(node)) {
    console.log('Found:', node.type)
  }
})
```

When running this with a composite matcher that checks for multiple node types, I'm getting incorrect matches. Some nodes that should match aren't being detected, while the logic seems to skip certain valid nodes.

### Expected behavior

The composite matcher should correctly identify all nodes that match any of the specified criteria. Each check should be evaluated properly and return true if any of them match.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

This seems like it might be related to how the internal checking logic iterates through multiple test conditions. The behavior is inconsistent and doesn't match what I'd expect from an "any" type matcher.

---
Repository: /testbed
