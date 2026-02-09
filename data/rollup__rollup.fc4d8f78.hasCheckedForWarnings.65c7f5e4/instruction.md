# Bug Report

### Describe the bug

I'm seeing duplicate warnings being logged when using tagged template expressions in my code. It looks like the same warning is being emitted multiple times for the same tagged template literal, which is cluttering up the build output.

### Reproduction

```js
const result = someTag`template ${value} string`;
```

When this code is bundled, I'm getting the same warning repeated multiple times instead of just once.

### Expected behavior

Each warning should only be shown once per tagged template expression, not multiple times. The warning system should track which expressions have already been checked and skip them on subsequent passes.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
