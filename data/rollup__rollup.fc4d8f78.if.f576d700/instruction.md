# Bug Report

### Describe the bug

When bundling ES modules, exports without expressions are being incorrectly added to the export block. This causes `const undefined = undefined;` statements to appear in the generated output, which breaks the build.

### Reproduction

```js
// input module
export { foo } from './other.js';

// generated output contains:
// const foo = undefined;
// export { foo };
```

The bundler is generating invalid code where it tries to declare constants with `undefined` values for re-exported bindings that don't have their own expressions.

### Expected behavior

Re-exports should be handled correctly without generating unnecessary constant declarations. The output should only include the export statement itself when there's no local expression to assign.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
