# Bug Report

### Describe the bug

I'm experiencing an issue where certain markdown constructs are being incorrectly processed or not disabled as expected. It seems like the `disable` export is pointing to the wrong implementation, causing unexpected parsing behavior.

### Reproduction

When trying to use the remark parser with disabled constructs, the configuration doesn't seem to work properly:

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'

const processor = unified()
  .use(remarkParse)
  .use(() => (tree, file) => {
    // Trying to access disable functionality
    // Results in unexpected behavior
  })

const result = processor.processSync('# Test')
```

The parser appears to be using an incorrect reference internally, which leads to constructs not being properly disabled when they should be.

### Expected behavior

The `disable` export should correctly reference the disable functionality and allow markdown constructs to be properly disabled during parsing.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
