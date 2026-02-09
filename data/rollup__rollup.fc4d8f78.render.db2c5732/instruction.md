# Bug Report

### Describe the bug

I'm experiencing an issue with conditional statement rendering where the wrong branch is being kept after tree-shaking. When I have an if-else statement with a constant condition, the bundler is keeping the wrong branch in the output.

### Reproduction

```js
const DEBUG = false;

if (DEBUG) {
  console.log('Debug mode');
} else {
  console.log('Production mode');
}
```

After bundling with tree-shaking enabled, the output includes the `if` branch (debug mode) instead of the `else` branch (production mode), even though `DEBUG` is clearly `false`.

### Expected behavior

When the condition evaluates to `false`, the consequent branch should be removed and the alternate branch should be kept in the bundled output. The bundler should output:

```js
console.log('Production mode');
```

Instead, it seems to be doing the opposite and keeping the wrong branch.

### Additional context

This appears to be related to how the bundler handles constant conditions in if-else statements during the tree-shaking process. The logic for determining which branch to keep seems inverted.

---
Repository: /testbed
