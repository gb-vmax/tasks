# Bug Report

### Describe the bug

I'm encountering an issue with leaf directives in remark-directive where the parser seems to be calling functions with incorrect context. When processing leaf directives in markdown, I'm getting unexpected behavior that suggests the `this` context is being bound incorrectly.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')
const remarkDirective = require('remark-directive')

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = `
::leafDirective[content]
`

const ast = processor.parse(markdown)
const result = processor.runSync(ast)

// Leaf directive is not processed correctly
console.log(result)
```

### Expected behavior

Leaf directives should be parsed and processed correctly with the proper context binding. The parser should handle the directive node creation without errors.

### Additional context

This seems to affect specifically leaf directives - container directives and text directives appear to work fine. The issue manifests when the parser tries to enter a leaf directive node during the parsing phase.

---
Repository: /testbed
