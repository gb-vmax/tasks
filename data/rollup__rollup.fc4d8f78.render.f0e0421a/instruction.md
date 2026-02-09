# Bug Report

### Describe the bug

When tree-shaking removes an unused label from a labeled statement, the generated code includes extra whitespace or characters before the body of the statement. This results in malformed output that may break the code structure.

### Reproduction

```js
// Input code with a labeled statement where the label is not referenced
myLabel: {
  console.log('hello');
}

// After tree-shaking removes the unused label, the output contains
// unexpected characters/whitespace before the console.log statement
```

The issue occurs when:
1. A labeled statement exists in the code
2. The label is not referenced anywhere (making it eligible for removal)
3. Tree-shaking removes the label
4. The remaining code block has incorrect leading content

### Expected behavior

When an unused label is removed during tree-shaking, only the label and colon should be removed, leaving clean code:

```js
{
  console.log('hello');
}
```

Instead, extra content from before the label appears to be left in the output.

---
Repository: /testbed
