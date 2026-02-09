# Bug Report

### Describe the bug

I'm encountering an issue where side effects in my code are not being detected correctly. It seems like the tree-shaking is removing code that should be kept because it has side effects.

### Reproduction

```js
// This code should be preserved because it has side effects
const arr = [
  console.log('effect 1'),
  console.log('effect 2'),
  console.log('effect 3')
];

// After bundling, all the console.log statements are removed
// even though they should be kept
```

When I bundle this code, the console.log statements are being tree-shaken away even though they clearly have side effects and should be preserved in the output.

### Expected behavior

Code with side effects should be detected and preserved during the bundling process. The console.log statements should appear in the final bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
