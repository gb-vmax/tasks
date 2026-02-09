# Bug Report

### Describe the bug

I'm encountering an issue with static blocks in classes where the closing brace is being rendered at the wrong position. When a static block contains code, the output appears to be truncated or malformed.

### Reproduction

```js
class MyClass {
  static {
    console.log('initialization');
    this.value = 42;
  }
}
```

After bundling/processing, the static block output is incorrect - the closing brace position seems off and the block doesn't render properly.

### Expected behavior

The static block should be rendered correctly with all its contents intact and proper brace positioning. The output should maintain the structure:

```js
class MyClass {
  static {
    console.log('initialization');
    this.value = 42;
  }
}
```

### Additional context

This seems to affect any static block that has a body with statements. Empty static blocks might work fine, but blocks with actual code inside are producing unexpected output.

---
Repository: /testbed
