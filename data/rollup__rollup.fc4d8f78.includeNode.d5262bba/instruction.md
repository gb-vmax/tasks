# Bug Report

### Bug with function call deoptimization

I've encountered an issue where function calls are not being properly deoptimized during tree-shaking. It seems like the deoptimization logic is being applied at the wrong time, which causes some side effects to not be tracked correctly.

### Reproduction

```js
// Example that demonstrates the issue
function sideEffect() {
  console.log('This should be included');
}

function wrapper() {
  sideEffect();
}

// When this is called, the side effects aren't properly tracked
wrapper();
```

The problem appears to be that deoptimization happens after the callee path is already included, so some information about side effects gets lost.

### Expected behavior

Function calls should be deoptimized before their callee paths are included, ensuring that all side effects and dependencies are properly tracked during the inclusion phase.

### Additional context

This seems to affect how the bundler determines which code can be safely removed during tree-shaking. In some cases, code with side effects is being incorrectly eliminated or not properly marked for inclusion.

---
Repository: /testbed
