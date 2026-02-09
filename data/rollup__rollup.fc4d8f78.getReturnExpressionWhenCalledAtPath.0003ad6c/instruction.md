# Bug Report

### Describe the bug

I'm experiencing an issue with string method calls on unknown literal strings. When calling methods like `.toString()` or `.charAt()` on string literals, the return type inference seems to be broken and I'm getting unexpected behavior in my code analysis.

### Reproduction

```js
const myString = "hello";
const result = myString.charAt(0); // Should return a string
const result2 = myString.toString(); // Should return a string
```

When analyzing code like this, the type inference for string method calls doesn't work correctly. It seems like the return type is not being properly resolved.

### Expected behavior

String methods called on literal strings should properly infer their return types. Methods like `charAt`, `toString`, `substring`, etc. should all return the appropriate types based on the string prototype.

### Additional context

This appears to affect all string prototype methods when called on literal string values. The issue manifests during static analysis of the code.

---
Repository: /testbed
