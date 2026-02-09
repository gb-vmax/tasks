# Bug Report

### Describe the bug

I'm experiencing an issue with autolink parsing where the tokenizer seems to get stuck in an infinite loop. When processing markdown content with autolinks (like `<http://example.com>`), the parser hangs and never completes.

### Reproduction

```js
import {remark} from 'remark'

const markdown = '<http://example.com>'

// This hangs indefinitely
const result = remark().processSync(markdown)
console.log(result)
```

### Expected behavior

The autolink should be parsed correctly and the processing should complete without hanging. The parser should tokenize the autolink and continue processing the rest of the document.

### Additional context

This seems to affect any markdown content containing autolinks. The issue appears to be related to the tokenization phase - the process never returns and eventually times out or needs to be killed manually.

---
Repository: /testbed
