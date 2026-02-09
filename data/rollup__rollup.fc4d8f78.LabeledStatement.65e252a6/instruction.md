# Bug Report

### Describe the bug

I'm encountering an issue with labeled statements in my code. It seems like labels are being incorrectly included or excluded during the tree-shaking process, causing unexpected behavior in the bundled output.

### Reproduction

```js
function test() {
  myLabel: {
    if (condition) {
      break myLabel;
    }
    console.log('This should be included');
  }
}
```

When bundling code with labeled statements that contain break statements, the label itself is not being included in the output when it should be. This results in invalid JavaScript being generated.

### Expected behavior

When a labeled statement contains a break statement that references the label, the label should be properly included in the bundled output. The tree-shaking logic should recognize that the label is necessary and preserve it.

### Additional context

This appears to be related to how the bundler determines whether a label is "used" or not. The logic for tracking which labels need to be included seems to be inverted - labels that are referenced by break statements are being excluded instead of included.

---
Repository: /testbed
