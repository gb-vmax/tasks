# Bug Report

### Describe the bug

I'm experiencing an issue with code generation where block statements with multiple statements are not being output correctly. It appears that the last statement in a block is being omitted from the generated code.

### Reproduction

When generating code from an AST that contains a BlockStatement with multiple statements, only the statements up to (but not including) the final one are written to the output.

For example, with a block like:
```js
{
  const a = 1;
  const b = 2;
  const c = 3;
}
```

The generated output is missing the last statement and the closing brace seems to be positioned incorrectly.

### Expected behavior

All statements within a block should be included in the generated output, with proper indentation and the closing brace in the correct position.

### Additional context

This seems to affect any BlockStatement node that has 2 or more statements in its body array. Single-statement blocks and empty blocks appear to work fine.

---
Repository: /testbed
