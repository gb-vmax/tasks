# Bug Report

### Describe the bug

After a recent update, the markdown parser appears to be broken. When trying to parse markdown content, I'm getting unexpected errors or the parser just stops working completely.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()
const result = processor.processSync('# Hello World\n\nThis is a test.')
console.log(result)
```

When running this code, the parser fails to process the markdown correctly. It seems like the tokenizer isn't functioning properly anymore.

### Expected behavior

The markdown should be parsed successfully and return the expected AST structure. This was working fine in previous versions.

### Additional context

This appears to have started happening recently. The parser seems to get stuck or fail when trying to tokenize markdown constructs. Not sure if this is related to recent changes in the tokenization logic.

---
Repository: /testbed
