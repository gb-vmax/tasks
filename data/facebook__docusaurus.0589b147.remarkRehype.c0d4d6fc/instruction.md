# Bug Report

### Describe the bug

I'm experiencing an issue with the `remarkRehype` function where it's not returning the transformed tree properly. When using `remarkRehype` without a destination processor, the function completes but doesn't return anything, causing the pipeline to break.

### Reproduction

```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkRehype from 'remark-rehype'

const processor = unified()
  .use(remarkParse)
  .use(remarkRehype)

const result = await processor.process('# Hello')
console.log(result) // undefined or missing tree
```

The transformation runs but the resulting tree is not available for further processing in the pipeline.

### Expected behavior

The function should return the transformed HAST tree so it can be used by subsequent plugins or processors in the chain. The tree should be accessible in the result.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
