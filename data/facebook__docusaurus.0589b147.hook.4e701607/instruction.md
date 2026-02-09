# Bug Report

### Describe the bug

After a recent update, the remark parser appears to be completely broken. When trying to parse any markdown content, the parser fails to process the input correctly and doesn't return expected results.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()
const result = processor.processSync('# Hello World')

console.log(result)
// Expected: parsed AST with heading node
// Actual: incomplete/malformed output or error
```

### Expected behavior

The parser should correctly tokenize and parse markdown syntax, returning a proper AST structure. Basic constructs like headings, lists, and paragraphs should be recognized and processed.

### Additional context

This seems to affect all markdown parsing operations. Even simple single-line markdown fails to parse correctly. The tokenizer factory appears to not be completing its execution properly - constructs are not being handled through their full lifecycle.

---
Repository: /testbed
