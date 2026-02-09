# Bug Report

### Describe the bug

I'm experiencing an issue with parameter name validation in function declarations. When I define a function with duplicate parameter names, the parser is not catching this error correctly. It seems like the duplicate parameter detection is broken.

### Reproduction

```js
function test(a, a) {
  return a;
}
```

The above code should raise an error about duplicate parameter names, but it's being accepted without any warnings or errors.

Also noticed that when using parenthesized expressions in binding contexts, the binding type is not being preserved correctly, which might be related.

### Expected behavior

The parser should detect and report duplicate parameter names with an "Argument name clash" error. This is a syntax error in strict mode and should be caught during parsing.

### Additional context

This appears to have started recently. The duplicate parameter detection was working correctly before, so this might be a regression.

---
Repository: /testbed
