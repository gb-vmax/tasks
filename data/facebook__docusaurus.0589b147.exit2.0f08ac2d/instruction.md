# Bug Report

### Describe the bug
When converting markdown AST to string using `toMarkdown()`, the output is missing content or producing malformed markdown. It seems like the internal stack state is getting corrupted during the conversion process, causing nested structures to be improperly handled.

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
            {type: 'text', value: 'bold text'}
          ]
        }
      ]
    }
  ]
}

const result = toMarkdown(tree)
console.log(result)
// Expected: **bold text**
// Actual: Incomplete or malformed output
```

### Expected behavior
The markdown output should correctly preserve all nested structures and produce valid markdown syntax. Nested elements like lists, emphasis, links, etc. should be properly serialized.

### Additional context
This appears to affect any markdown tree with nested block or inline elements. The more deeply nested the structure, the more broken the output becomes. Simple flat structures seem to work fine, but anything with 2+ levels of nesting produces incorrect results.

---
Repository: /testbed
