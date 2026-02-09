# Bug Report

### Describe the bug

I'm experiencing an issue with the `strong` element handler in remark-rehype. When processing markdown with bold text (using `**` or `__`), the resulting HTML element seems to have incorrect or missing position information.

### Reproduction

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'
import remarkRehype from 'remark-rehype'

const processor = unified()
  .use(remarkParse)
  .use(remarkRehype)

const result = processor.processSync('This is **bold text**')

// The strong element doesn't have the expected position data
console.log(result)
```

When I parse markdown containing bold text, the position information on the generated `<strong>` element appears to be incorrect or not properly transferred from the markdown AST node.

### Expected behavior

The `<strong>` element should have accurate position information that corresponds to the original markdown source location. This is important for source mapping and error reporting.

### Additional context

This seems to affect specifically the bold/strong text transformation. Other inline elements appear to work correctly. The issue might be related to how the node data is being applied or patched during the transformation process.

---
Repository: /testbed
