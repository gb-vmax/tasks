# Bug Report

### Describe the bug

When parsing GFM (GitHub Flavored Markdown) strikethrough syntax, the output contains an unexpected `emphasis` node wrapping the `delete` node. This appears to be adding an extra layer to the AST that shouldn't be there.

### Reproduction

```js
import remarkParse from 'remark-parse'
import remarkGfm from 'remark-gfm'
import { unified } from 'unified'

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)

const result = processor.parse('~~strikethrough text~~')
console.log(JSON.stringify(result, null, 2))
```

### Expected behavior

The AST should contain a `delete` node directly without any intermediate `emphasis` wrapper:

```json
{
  "type": "delete",
  "children": [
    {
      "type": "text",
      "value": "strikethrough text"
    }
  ]
}
```

### Actual behavior

The AST contains an extra `emphasis` node that wraps the `delete` node, creating an incorrect structure.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

This seems to have appeared recently and is causing issues with markdown processing pipelines that expect the standard GFM AST structure.

---
Repository: /testbed
