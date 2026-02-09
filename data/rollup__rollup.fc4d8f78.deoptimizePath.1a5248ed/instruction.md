# Bug Report

### Describe the bug

I'm experiencing an issue where tree-shaking is not working correctly for destructured parameters in certain cases. When accessing nested properties on function parameters, Rollup seems to incorrectly include code that should have been eliminated.

### Reproduction

```js
function processData({ user }) {
  if (user.profile.name) {
    console.log('has name');
  }
}

// This should be tree-shaken out since it's never called
processData({ user: { profile: { name: 'test' } } });
```

The code above gets included in the bundle even when it's in a conditional branch that should be eliminated. It looks like the issue occurs specifically when there are multiple levels of property access on destructured parameters.

### Expected behavior

Dead code with nested property accesses on parameters should be properly eliminated during tree-shaking, just like it works with simpler property accesses.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
