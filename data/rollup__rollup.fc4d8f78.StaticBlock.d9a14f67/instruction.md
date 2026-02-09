# Bug Report

### Describe the bug

I'm experiencing an issue with static blocks in class declarations where the first statement inside a static block appears to be getting skipped or ignored during processing. This seems to affect both side effect detection and code generation.

### Reproduction

```js
class MyClass {
  static {
    console.log('First statement');
    console.log('Second statement');
  }
}
```

When bundling code with a static block, only statements after the first one seem to be processed correctly. If there's only a single statement in the static block, it gets completely ignored.

### Expected behavior

All statements within a static block should be processed, including the first one. A static block with a single statement should not be treated as empty.

### Additional context

This appears to affect:
- Side effect analysis (first statement's effects are not detected)
- Code rendering (static blocks with only one statement may not render correctly)

The issue seems to have been introduced recently as this was working fine in earlier versions.

---
Repository: /testbed
