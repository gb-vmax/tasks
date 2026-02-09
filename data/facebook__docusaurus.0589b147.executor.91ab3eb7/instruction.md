# Bug Report

### Describe the bug

I'm experiencing an issue with the remark processor where transformed trees are being replaced with the original tree instead of the output tree. When running transformations, the result I get back is always the original input tree, not the transformed version.

### Reproduction

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'

const processor = unified()
  .use(remarkParse)
  .use(() => (tree) => {
    // Transform the tree - add a new node
    tree.children.push({
      type: 'paragraph',
      children: [{type: 'text', value: 'Added by transformer'}]
    })
    return tree
  })

const input = '# Original heading'
const result = await processor.process(input)

// Expected: tree should include the added paragraph
// Actual: only contains the original heading
console.log(result)
```

### Expected behavior

The processor should return the transformed tree with modifications applied by the transformer plugins. In the example above, the output should include both the original heading and the newly added paragraph node.

### System Info
- remark version: 15.0.1
- Node.js version: Latest

This seems to have started happening recently. The transformers are running but their output is being ignored somehow.

---
Repository: /testbed
