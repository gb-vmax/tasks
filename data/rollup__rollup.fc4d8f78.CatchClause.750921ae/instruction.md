# Bug Report

### Describe the bug

I'm encountering an issue with variable scoping in catch clauses. It appears that variables declared in the catch block are not being properly isolated from the catch parameter scope.

### Reproduction

```js
try {
  throw new Error('test');
} catch (e) {
  const e = 'shadowed'; // Should be allowed in the catch body
  console.log(e);
}
```

When bundling code like this, I'm getting unexpected behavior where the catch parameter and variables in the catch block body seem to share the same scope, which shouldn't be the case according to JavaScript semantics.

### Expected behavior

The catch clause should have two distinct scopes:
1. A parameter scope for the caught exception (e.g., `e`)
2. A separate body scope for the catch block itself

Variables declared in the catch block body should be able to shadow the catch parameter without conflicts, just like how regular JavaScript works.

### Additional context

This seems to affect how the bundler handles variable declarations and references within catch blocks. The catch parameter and catch body should maintain separate scoping contexts.

---
Repository: /testbed
