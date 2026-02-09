# Bug Report

### Describe the bug

I'm encountering an issue when bundling files that start with a shebang (`#!`). The bundler seems to be removing too much content from the beginning of the file, causing the output to be malformed or incomplete.

### Reproduction

Create a file with a shebang line followed by code:

```js
#!/usr/bin/env node

console.log('Hello, world!');
```

When this file is processed, the output is corrupted - it appears that content beyond just the shebang line is being removed.

### Expected behavior

Only the shebang line itself should be removed from the output. The actual code following the shebang should remain intact and be properly bundled.

### Additional context

This seems to happen specifically when the file starts with `#!`. Regular files without shebangs process correctly. The issue might be related to how the start position is calculated after detecting the shebang.

---
Repository: /testbed
