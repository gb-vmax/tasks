# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing in remark-directive. When using leaf directives (like `:directive[label]{attributes}`), the parser seems to be handling whitespace incorrectly after the attributes section, which causes parsing to fail or behave unexpectedly.

### Reproduction

```js
const unified = require('unified')
const markdown = require('remark-parse')
const directive = require('remark-directive')

const processor = unified()
  .use(markdown)
  .use(directive)

// This directive with attributes and trailing content fails to parse correctly
const text = ':myDirective[some label]{key=value} some text after'

const result = processor.parse(text)
console.log(result)
```

The directive doesn't seem to be properly terminated after the attributes block, leading to incorrect AST output.

### Expected behavior

The leaf directive should be correctly parsed and closed after the attributes section, with any trailing whitespace and content handled appropriately. The parser should properly recognize where the directive ends and regular content begins.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
