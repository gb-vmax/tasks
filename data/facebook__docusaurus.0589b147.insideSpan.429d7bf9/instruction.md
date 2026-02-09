# Bug Report

### Describe the bug

I'm getting a runtime error when trying to use the remark parser. It seems like there's an issue with how one of the construct exports is being handled. The parser crashes immediately when trying to process markdown content.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()
const result = processor.processSync('# Hello World')
```

When running this code, I get an error that `insideSpan` is not a function or something similar. The parser fails to initialize properly.

### Expected behavior

The markdown processor should parse the content without throwing errors. This was working fine in previous versions.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
