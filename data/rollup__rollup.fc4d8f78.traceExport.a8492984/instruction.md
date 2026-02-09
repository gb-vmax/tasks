# Bug Report

### Describe the bug

I'm experiencing an issue where named exports are not being resolved correctly. When I try to import a named export from a module, I get an error saying the export doesn't exist, even though it's clearly defined in the source file.

### Reproduction

```js
// module.js
export const MyComponent = () => { /* ... */ }
export const AnotherComponent = () => { /* ... */ }

// consumer.js
import { MyComponent } from './module.js'
```

The import fails to resolve `MyComponent` even though it's exported. This seems to happen inconsistently - sometimes it works, sometimes it doesn't.

### Expected behavior

Named exports should be resolved correctly regardless of their casing or whitespace. The bundler should find the exact export name as written in the source code.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
