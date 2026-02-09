# Bug Report

### Describe the bug

When generating SystemJS output with exactly one export, there's an issue with the formatting. The generated code includes extra newlines that shouldn't be there, which differs from the output when there are zero or multiple exports.

### Reproduction

```js
// Bundle configuration with a single named export
export const myValue = 42;
```

When this is bundled with the SystemJS output format, the generated code has inconsistent formatting compared to bundles with zero or multiple exports. The single export case adds extra newlines after the exports statement that aren't present in other cases.

### Expected behavior

The formatting should be consistent across all cases (0, 1, or multiple exports). A single export should not have different trailing newlines compared to the multiple exports case.

### System Info
- Rollup version: latest
- Output format: system

---
Repository: /testbed
