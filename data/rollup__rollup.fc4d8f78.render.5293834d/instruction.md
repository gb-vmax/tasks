# Bug Report

### Describe the bug

When bundling a file that starts with a shebang (`#!/usr/bin/env node`), the output code is getting corrupted. The first character after the shebang line is being removed, causing syntax errors in the generated bundle.

### Reproduction

Create a file with a shebang:

```js
#!/usr/bin/env node
const greeting = 'Hello World';
console.log(greeting);
```

After bundling, the output becomes:

```js
onst greeting = 'Hello World';
console.log(greeting);
```

Notice the `c` from `const` is missing, making the code invalid.

### Expected behavior

The shebang should be removed cleanly without affecting the first line of actual code. The output should be:

```js
const greeting = 'Hello World';
console.log(greeting);
```

### Additional context

This seems to be a regression - it was working fine in previous versions. The issue only occurs when the file starts with a shebang line.

---
Repository: /testbed
