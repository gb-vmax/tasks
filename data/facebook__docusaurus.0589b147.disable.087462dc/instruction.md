# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the remark parser. It appears that there's an issue with how the `disable` export is being handled in the constructs module. The parser fails to load and throws an error about unexpected token syntax.

### Reproduction

```js
import {remark} from 'remark';

const processor = remark();
const result = processor.processSync('# Hello World');
```

When running this code, I get a syntax error related to the module exports. The error message indicates there's an issue with the object destructuring syntax in the export statement.

### Expected behavior

The remark processor should initialize correctly and be able to parse markdown content without throwing syntax errors during module loading.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have appeared recently - the same code was working before. Any help would be appreciated!

---
Repository: /testbed
