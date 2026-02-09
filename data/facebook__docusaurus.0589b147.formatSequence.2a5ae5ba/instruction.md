# Bug Report

### Describe the bug

I'm encountering an issue with generated JavaScript output where function parameter lists or sequence expressions are being formatted incorrectly. The closing parenthesis appears before the actual parameters are written, resulting in malformed code.

### Reproduction

When processing MDX content that involves function calls or sequence expressions with multiple parameters, the generated output has incorrect parenthesis placement:

```js
// Expected output:
(param1, param2, param3)

// Actual output:
()(, param1, param2, param3)
```

The closing `)` appears immediately after the opening `(`, followed by the parameters with an extra leading comma.

### Expected behavior

Parameter sequences should be properly formatted with:
1. Opening parenthesis
2. All parameters separated by commas (no leading comma)
3. Closing parenthesis at the end

The output should look like `(param1, param2, param3)` not `()(, param1, param2, param3)`.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: 18.x

This appears to have started recently and is breaking the generated code output. Any MDX files with function calls or similar constructs are affected.

---
Repository: /testbed
