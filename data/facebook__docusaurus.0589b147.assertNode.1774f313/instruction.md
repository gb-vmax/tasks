# Bug Report

### Describe the bug

I'm encountering an issue with node validation in the MDX parser. When passing valid node objects to the parser, I'm getting unexpected `TypeError` exceptions saying "Expected node, got `[object Object]`".

### Reproduction

```js
const validNode = {
  type: 'element',
  tagName: 'div',
  children: []
}

// This throws an error even though the node is valid
// TypeError: Expected node, got `[object Object]`
processNode(validNode)
```

### Expected behavior

Valid node objects (plain objects with a `type` property that is a string) should be accepted without throwing errors. The validation should only reject invalid nodes that are either not plain objects or don't have a string `type` property.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: 18.x

---
Repository: /testbed
