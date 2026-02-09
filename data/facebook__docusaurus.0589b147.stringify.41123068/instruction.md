# Bug Report

### Describe the bug

The `stringify()` method is throwing an error when trying to compile markdown content. It appears that the compiler assertion is failing even when a valid compiler is configured.

### Reproduction

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'
import remarkStringify from 'remark-stringify'

const processor = unified()
  .use(remarkParse)
  .use(remarkStringify)

const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [{type: 'text', value: 'Hello world'}]
    }
  ]
}

// This throws an error
const result = processor.stringify(tree)
```

### Expected behavior

The `stringify()` method should successfully compile the tree into a markdown string without throwing errors when a compiler is properly configured.

### Additional context

This seems to have started happening recently. The error occurs during the assertion check for the compiler, even though the compiler plugin is registered and should be available.

---
Repository: /testbed
