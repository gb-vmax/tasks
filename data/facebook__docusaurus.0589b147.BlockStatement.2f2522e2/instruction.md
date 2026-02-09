# Bug Report

### Describe the bug

I'm seeing incorrect indentation when generating code with nested block statements. The closing brace appears to be indented at the wrong level - it's one level too deep compared to where it should be.

### Reproduction

When processing JavaScript AST nodes with nested blocks, the generated output has misaligned closing braces:

```js
// Expected output:
function example() {
  if (condition) {
    doSomething();
  }
}

// Actual output:
function example() {
  if (condition) {
    doSomething();
    }  // <- this brace is indented too far
  }    // <- this one too
```

The issue seems to affect any code with block statements. The opening braces are fine, but the closing braces have an extra level of indentation.

### Expected behavior

Closing braces should align with the indentation level of their corresponding opening statement, not be indented one level deeper.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
