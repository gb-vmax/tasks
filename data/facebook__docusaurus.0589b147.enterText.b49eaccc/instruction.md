# Bug Report

### Describe the bug

I'm experiencing an issue with text directives in remark-directive. When parsing markdown with text directives (like `:directive[content]`), the parser crashes with a TypeError saying that `this.call` is not a function.

### Reproduction

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'
import remarkDirective from 'remark-directive'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = 'Some text with :textDirective[content] in it.'

// This throws an error
processor.processSync(markdown)
```

### Expected behavior

The text directive should be parsed correctly without throwing an error, similar to how leaf directives and container directives work.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
