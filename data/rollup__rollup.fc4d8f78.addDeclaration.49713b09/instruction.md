# Bug Report

### Describe the bug

The code appears to be completely broken after a recent change. When trying to use catch blocks with var declarations, the build fails with a syntax error. It looks like the `addDeclaration` method in `CatchBodyScope` got corrupted or truncated.

### Reproduction

```js
try {
  throw new Error('test');
} catch (e) {
  var x = 1;
  console.log(x);
}
```

Any code that uses a `var` declaration inside a catch block will cause the bundler to fail during the build process.

### Expected behavior

The code should build successfully and handle var declarations in catch blocks correctly, including proper hoisting behavior.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a critical regression that completely breaks the build. The source file appears to have been accidentally truncated or corrupted.

---
Repository: /testbed
