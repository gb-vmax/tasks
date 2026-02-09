# Bug Report

### Describe the bug

I'm encountering a runtime error when using the remark markdown processor. The application crashes with an error about `result` not being defined when trying to convert a markdown tree back to a string.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()
const tree = processor.parse('# Hello World')

// This throws an error
const markdown = processor.stringify(tree)
```

The error seems to happen during the stringification process. The code tries to access a variable before it's been declared/assigned.

### Expected behavior

The `stringify` method should successfully convert the markdown AST back to a markdown string without throwing any errors. It should return something like:

```
# Hello World
```

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
