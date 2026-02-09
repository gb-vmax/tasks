# Bug Report

### Describe the bug

I'm experiencing what appears to be an infinite recursion issue when working with variable declarators in certain scenarios. The bundler hangs indefinitely and eventually crashes with a stack overflow error.

### Reproduction

This seems to happen when processing code with destructured variable declarations that are later accessed or modified:

```js
const { foo } = obj;
foo.bar = 'value';
```

The bundler enters an infinite loop during the optimization phase and never completes. I have to kill the process manually.

### Expected behavior

The bundler should complete the optimization pass without hanging or crashing. The code should be processed normally like it was in previous versions.

### System Info
- Rollup version: latest from main branch
- Node version: 18.x
- OS: macOS

This is blocking our production build pipeline. Any help would be appreciated!

---
Repository: /testbed
