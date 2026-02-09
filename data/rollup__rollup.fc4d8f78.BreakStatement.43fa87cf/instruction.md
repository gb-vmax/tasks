# Bug Report

### Describe the bug

I'm encountering an issue with labeled break statements in switch cases. When a break statement has a label, the code flow analysis seems to be incorrect, causing the bundler to treat subsequent code as unreachable when it shouldn't be.

### Reproduction

```js
outer: switch (value) {
  case 'a':
    doSomething();
    break outer;
  case 'b':
    doSomethingElse();
    break;
}

// Code here is incorrectly treated as unreachable
console.log('This should execute');
```

The problem occurs specifically when using labeled break statements inside switch cases. The code after the switch block gets incorrectly marked as dead code and is removed from the bundle.

### Expected behavior

Code following a switch statement with labeled breaks should be included in the output bundle unless there's a genuine control flow reason to exclude it. The labeled break should only affect the control flow within the labeled block, not the code that comes after.

### Additional context

This appears to be related to how the AST handles break statements with labels. Regular break statements (without labels) work fine, and labeled breaks in other contexts (like loops) also seem to work correctly. The issue is specific to the combination of labeled breaks within switch statements.

---
Repository: /testbed
