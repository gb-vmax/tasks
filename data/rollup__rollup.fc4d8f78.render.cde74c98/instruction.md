# Bug Report

### Describe the bug

Tagged template expressions are being rendered in the wrong order, causing the template literal to appear before the tag function in the generated output.

### Reproduction

```js
const result = myTag`template ${value} string`;
```

When this code is processed, the output has the template literal rendered before the tag function, which breaks the syntax and produces invalid JavaScript.

### Expected behavior

The tag function should be rendered first, followed by the template literal, maintaining the correct syntax:
```js
myTag`template ${value} string`
```

Instead, the current output appears to render components in reverse order.

### Additional context

This seems to affect all tagged template expressions regardless of the tag function used. The generated code is syntactically invalid and will fail to execute.

---
Repository: /testbed
