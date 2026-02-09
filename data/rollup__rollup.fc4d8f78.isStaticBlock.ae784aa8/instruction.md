# Bug Report

### Describe the bug

I'm encountering an issue where static blocks in classes are not being processed correctly. It seems like the bundler is treating non-static blocks as static blocks and vice versa, which is causing unexpected behavior in the output.

### Reproduction

```js
class MyClass {
  static {
    console.log('This is a static block');
  }
  
  constructor() {
    console.log('Constructor');
  }
}
```

When bundling code that contains static blocks, the output is incorrect. The static block logic appears to be inverted - statements that should be identified as static blocks are not being recognized, and statements that aren't static blocks are being incorrectly identified as such.

### Expected behavior

Static blocks should be correctly identified and processed. The `isStaticBlock` utility should return `true` for actual static block statements and `false` for everything else.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
