# Bug Report

### Describe the bug

I'm encountering an issue with generated JavaScript code where return statements are missing semicolons and have incorrect spacing when the returned value is an identifier.

### Reproduction

When processing MDX files that contain return statements with identifiers, the generated JavaScript output is malformed:

```js
// Input MDX with a function that returns an identifier
function example() {
  return value
}

// Generated output is missing semicolon and has no space:
// returnvalue
```

The return statement is being concatenated with the identifier without proper spacing, and the semicolon at the end of the statement is also missing.

### Expected behavior

The generated code should properly format return statements with:
1. A space between `return` and the identifier
2. A semicolon at the end of the statement

Expected output:
```js
return value;
```

### Additional context

This seems to affect return statements specifically when the argument is an identifier. Other types of return arguments might not be affected, but the missing semicolon appears to be a general issue with all return statements.

---
Repository: /testbed
