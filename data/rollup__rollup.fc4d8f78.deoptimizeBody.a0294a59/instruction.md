# Bug Report

### Describe the bug

I'm experiencing an issue where block statements are being deoptimized when they shouldn't be. This is causing unexpected behavior in code optimization - it seems like the bundler is applying deoptimizations too aggressively, even to code blocks that should remain optimized.

### Reproduction

```js
// Example code that triggers the issue
function test() {
  {
    const x = 1;
    const y = 2;
    return x + y;
  }
}
```

When bundling code with nested block statements, the optimization behavior is inverted from what's expected. Blocks that should be optimized are being deoptimized, leading to larger bundle sizes and potentially slower runtime performance.

### Expected behavior

Block statements should only be deoptimized when necessary (e.g., when they contain side effects or dynamic behavior that prevents optimization). Simple block scopes with pure operations should remain optimized.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
