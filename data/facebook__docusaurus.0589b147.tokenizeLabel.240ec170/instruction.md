# Bug Report

### Describe the bug

I'm experiencing an issue with directive container labels in remark-directive. It seems like the label parsing behavior has changed and is now accepting invalid syntax that should be rejected.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')
const remarkDirective = require('remark-directive')

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

// This should fail but is being accepted
const result = processor.parse(':::note[invalid label syntax]\ncontent\n:::')
```

When parsing directive containers with labels, the parser is now accepting label formats that should be rejected according to the spec. The label validation appears to be inverted - it's allowing malformed labels while potentially rejecting valid ones.

### Expected behavior

The parser should properly validate directive container labels and reject invalid label syntax. Labels that don't conform to the expected format should trigger a parsing error or be treated as invalid.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
