# Bug Report

### Describe the bug

After a recent update, the markdown parser is throwing an error when trying to process documents. The error occurs immediately when attempting to parse any markdown content, making the parser completely unusable.

### Reproduction

```js
import {remark} from 'remark';

const processor = remark();
const result = processor.processSync('# Hello World');
```

This throws an error related to `disable` not being a function. The parser fails to initialize properly and cannot process any markdown input.

### Expected behavior

The markdown parser should successfully process the input and return the parsed result without throwing any errors during initialization.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
