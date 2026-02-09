# Bug Report

### Describe the bug

I'm experiencing an issue with the code generator where `return` statements with arguments are producing invalid JavaScript syntax. The semicolon is being placed before the return value instead of after it.

### Reproduction

When processing code with return statements that have arguments, the generated output is malformed:

```js
// Input code (expected)
return someValue;

// Generated output (actual)
return;someValue;
```

This creates a syntax error because the return statement is terminated early with a semicolon, and then the value expression follows as a separate statement.

### Expected behavior

Return statements should generate valid JavaScript with the semicolon placed after the argument:
```js
return someValue;
```

Not:
```js
return;someValue;
```

### Additional context

This appears to affect any return statement that has an argument. Return statements without arguments (just `return;`) seem to work correctly.

---
Repository: /testbed
