# Bug Report

### Describe the bug

I'm experiencing an issue with object expression rendering where empty objects `{}` are not being handled correctly. It seems like the code generation is adding extra wrapping or processing even when there are no properties to render.

### Reproduction

```js
const emptyObj = {};
// Empty object literals should be rendered as-is
// but they're getting extra processing/wrapping

const result = bundle({
  input: {
    code: 'export default {}'
  }
});
// The output is malformed or has unexpected transformations
```

Also seeing weird behavior where object properties that should be included in the output are being removed instead. Properties are disappearing from the final bundle even though they're clearly used.

### Expected behavior

Empty object literals should be rendered correctly without unnecessary transformations. Object properties that are included/used should appear in the output bundle.

### Additional context

This might be related to tree-shaking logic - it feels like the conditions for what gets included vs excluded are inverted somehow. Properties are being treated opposite to what they should be.

---
Repository: /testbed
