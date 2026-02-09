# Bug Report

### Describe the bug

When using the `using` declaration (explicit resource management), the disposal behavior is incorrect. The `using` keyword should call `Symbol.dispose` on the resource when it goes out of scope, but instead it's trying to call `Symbol.asyncDispose`, which is meant for `await using` declarations.

Similarly, `await using` declarations are incorrectly attempting to use `Symbol.dispose` instead of `Symbol.asyncDispose`.

### Reproduction

```js
class Resource {
  [Symbol.dispose]() {
    console.log('disposed');
  }
}

{
  using resource = new Resource();
  // Should call Symbol.dispose when exiting block
}
// Error: resource[Symbol.asyncDispose] is not a function
```

```js
class AsyncResource {
  async [Symbol.asyncDispose]() {
    console.log('async disposed');
  }
}

async function test() {
  await using resource = new AsyncResource();
  // Should call Symbol.asyncDispose when exiting block
}
// Error: resource[Symbol.dispose] is not a function
```

### Expected behavior

- `using` declarations should invoke `Symbol.dispose` on resources
- `await using` declarations should invoke `Symbol.asyncDispose` on resources

The disposal symbols appear to be swapped between synchronous and asynchronous resource management.

---
Repository: /testbed
