# Bug Report

### Describe the bug

When bundling files that start with a shebang (`#!`), the shebang line is not being properly removed from the output. The newline character after the shebang appears to be missing, causing the first line of actual code to be incorrectly positioned or merged with subsequent content.

### Reproduction

Create a file with a shebang:

```js
#!/usr/bin/env node

console.log('hello');
```

After bundling, the shebang removal seems incomplete - the newline handling appears broken and the output formatting is incorrect.

### Expected behavior

The shebang line (including the trailing newline) should be completely removed from the output, leaving the rest of the code properly formatted starting from the first line after the shebang.

### Additional context

This seems to affect files that have shebangs at the very beginning. The issue might be related to how the newline character position is calculated when removing the shebang prefix.

---
Repository: /testbed
