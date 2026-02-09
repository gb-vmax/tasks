# Bug Report

### Describe the bug

I'm encountering an issue where the rehype-stringify processor seems to fail when processing valid AST nodes. The processor appears to be calling the wrong handler or the invalid handler even when the node type is valid and registered.

### Reproduction

```js
const unified = require('unified')
const rehypeStringify = require('rehype-stringify')

const processor = unified().use(rehypeStringify)

const ast = {
  type: 'root',
  children: [
    {
      type: 'element',
      tagName: 'div',
      properties: {},
      children: []
    }
  ]
}

// This should work but throws an error or produces unexpected output
const result = processor.stringify(ast)
console.log(result)
```

### Expected behavior

The processor should correctly identify the node type and call the appropriate handler to generate the HTML string output. Valid AST nodes with proper `type` properties should be processed without errors.

### System Info

- rehype-stringify version: 10.0.0
- Node.js version: 18.x

This seems to have started happening recently and is blocking our documentation generation pipeline. Any help would be appreciated!

---
Repository: /testbed
