# Bug Report

### Describe the bug

I'm experiencing an issue with re-exports in ES module output. When using `export * from` or namespace re-exports, the generated code seems to be incorrectly categorizing the export specifiers. This causes the bundle to produce unexpected export statements.

### Reproduction

```js
// source.js
export * from './module-a';
export { default as something } from './module-b';
export * as namespace from './module-c';
```

When bundling this with ES output format, the generated export statements don't match the expected structure. The star exports and namespace re-exports appear to be getting mixed up or incorrectly identified.

### Expected behavior

The bundler should correctly distinguish between:
- Star exports (`export * from`)
- Namespace re-exports (`export * as name from`)
- Named re-exports (`export { name } from`)

Each type should generate the appropriate export statement in the output bundle.

### System Info
- Rollup version: latest
- Output format: ES modules

---
Repository: /testbed
