# Bug Report

### Describe the bug

When generating System module format output with exactly one export, the export is being duplicated in the output. The first export appears both in the singular `exports()` call and also gets included in the exports object, resulting in the same export being registered twice.

### Reproduction

```js
// Input module with single named export
export const foo = 'bar';

// Generated System output incorrectly produces:
exports('foo', foo);

exports({
  foo: foo
});

// Expected output should be just:
exports('foo', foo);
```

This happens specifically when there is exactly one export. With zero exports or multiple exports, the output is generated correctly.

### Expected behavior

When a module has a single named export, it should generate only the singular `exports()` call format, not both the singular format AND the object format.

### System Info
- Rollup version: latest
- Output format: system

---
Repository: /testbed
