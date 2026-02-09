# Bug Report

### Describe the bug

I'm experiencing an issue with tagged template expressions where the tag function and template literal are being rendered in the wrong order. The output code has the template literal appearing before the tag function, which produces invalid JavaScript syntax.

### Reproduction

```js
const result = myTag`template ${value} string`;
```

When this gets processed, the output is malformed with the template parts appearing before the tag function identifier.

### Expected behavior

The tag function should be rendered first, followed by the template literal, maintaining the correct syntax:
```js
myTag`template ${value} string`
```

Instead, the current behavior seems to reverse this order in the generated code.

### Additional context

This appears to affect all tagged template expressions regardless of the tag function used. The rendered output doesn't match valid JavaScript syntax for tagged templates.

---
Repository: /testbed
