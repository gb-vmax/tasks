# Bug Report

### Describe the bug

I'm encountering an issue with export statement parsing in MDX files. When exporting variables or functions, the parser seems to be handling them incorrectly, leading to unexpected behavior.

### Reproduction

```js
// This export statement causes issues
export const myVariable = 'test';
export function myFunction() {
  return 'hello';
}

// Named exports also affected
export { foo, bar, baz };
```

When I try to use these exports in my MDX files, the first exported item in named export lists appears to be skipped or not properly registered. Additionally, variable declarations are being treated differently than expected.

### Expected behavior

All export statements should be parsed correctly:
- Variable declarations should be properly identified and exported
- All items in named export lists should be processed, including the first one
- Function and other declaration exports should work as intended

### Additional context

This seems to have broken recently. My MDX files that were working before now fail to properly export their declarations. The issue appears to be related to how the parser validates and processes export statements.

---
Repository: /testbed
