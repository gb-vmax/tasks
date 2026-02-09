# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing in remark-directive where lazy continuation lines are being handled incorrectly. It seems like the parser is checking the wrong property when determining whether a line should be treated as lazy or not, which causes directives to fail parsing in certain scenarios.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')
const remarkDirective = require('remark-directive')

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = `
:::note
This is a note
with multiple lines
that should be parsed correctly
:::
`

const result = processor.parse(markdown)
console.log(result)
```

When parsing directives with multi-line content, the continuation lines are not being recognized properly. The parser seems to be treating lines that should be part of the directive content as something else, or vice versa.

### Expected behavior

The directive should correctly parse all lines within its block, including continuation lines. The lazy line detection should work properly to determine which lines belong to the directive content.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

This is causing issues with parsing container directives that span multiple lines. Any help would be appreciated!

---
Repository: /testbed
