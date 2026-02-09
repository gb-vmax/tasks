# Bug Report

### Describe the bug

I'm experiencing an issue with invalid annotation warnings in my build output. It seems like warnings are being suppressed when they should be shown, specifically for annotations that are NOT `pure` or `noSideEffects`.

### Reproduction

Given a source file with invalid annotations (not `pure` or `noSideEffects`):

```js
/*#__INVALID__*/ someFunction();
```

The bundler is not logging warnings for these invalid annotations as expected. The annotations are being removed from the output, but no warning is generated to alert developers about the issue.

### Expected behavior

When invalid annotations are encountered (that are not `pure` or `noSideEffects`), a warning should be logged to inform developers that these annotations are invalid and have been removed. Currently, it appears these warnings are being skipped entirely.

### System Info

- Rollup version: latest
- Node version: 18.x

This is causing confusion during development as invalid annotations are silently removed without any indication that something might be wrong with the code.

---
Repository: /testbed
