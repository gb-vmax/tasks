# Bug Report

### Describe the bug

I'm experiencing an issue with markdown indentation not working properly. When using the indentation functionality, the mapped values aren't being applied to the output - instead, the original unmapped values are being returned.

### Reproduction

```js
const lines = "line1\nline2\nline3";
const indented = indentLines(lines, (value) => '  ' + value);

console.log(indented);
// Expected: "  line1\n  line2\n  line3"
// Actual: "line1\nline2\nline3"
```

The indentation mapping function is being called but the result isn't being used. The original line values are pushed to the result array instead of the transformed values.

### Expected behavior

The mapping function should transform each line and the transformed values should appear in the final output. When I pass a function that adds indentation or any other transformation, those changes should be reflected in the returned string.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
