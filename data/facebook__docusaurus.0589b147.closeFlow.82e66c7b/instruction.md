# Bug Report

### Describe the bug

I'm experiencing a critical issue after the latest update where the markdown parser completely breaks. The application crashes immediately when trying to parse any markdown content, and it seems like some core functionality has been corrupted.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()
const result = processor.processSync('# Hello World')
```

This throws an error about `closeFlow` not being defined. It looks like something fundamental in the document initialization is broken.

### Expected behavior

The markdown should parse correctly without any errors. This was working fine in the previous version.

### Additional context

This started happening suddenly and I can't process any markdown at all now. The error mentions something about `closeFlow` being undefined, which suggests there might be an issue with how the flow content is being handled during document initialization.

Any help would be greatly appreciated as this is blocking our entire content pipeline!

---
Repository: /testbed
