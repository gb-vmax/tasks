# Bug Report

### Describe the bug

I'm experiencing an issue with variable declaration rendering where semicolons are being added incorrectly. When bundling code with variable declarations that already have semicolons, an extra semicolon is being appended, resulting in double semicolons in the output.

### Reproduction

```js
// Input code
const foo = 'bar';
const baz = 'qux';

// Expected output
const foo = 'bar';
const baz = 'qux';

// Actual output
const foo = 'bar';;
const baz = 'qux';;
```

This seems to happen specifically when:
1. Variable declarations are included in the bundle
2. The declarations are not exported
3. The original code already has semicolons

### Expected behavior

Variable declarations should maintain their original semicolons without duplication. If a semicolon already exists at the end of a declaration, no additional semicolon should be added.

### Additional context

This appears to be affecting the final bundle output and is creating invalid/malformed JavaScript in some cases. The issue seems related to how the bundler checks for existing semicolons when rendering variable declarations.

---
Repository: /testbed
