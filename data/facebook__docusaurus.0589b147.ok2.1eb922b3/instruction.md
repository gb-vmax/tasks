# Bug Report

### Describe the bug

I'm encountering an unexpected error when using the remark parser. The parser is throwing an error with the message "Unexpected error" during normal operation, which seems to be coming from an internal assertion function.

### Reproduction

```js
const remark = require('remark');

const processor = remark();
const result = processor.processSync('# Hello World');
```

Running this basic markdown parsing code results in an error being thrown instead of successfully parsing the content.

### Expected behavior

The markdown should be parsed successfully without throwing any errors. Basic markdown processing should work as it did in previous versions.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have started recently and is blocking my workflow. Any help would be appreciated!

---
Repository: /testbed
