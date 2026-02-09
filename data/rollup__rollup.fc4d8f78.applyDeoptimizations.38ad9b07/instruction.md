# Bug Report

### Describe the bug

I'm encountering an issue with class declarations where variable name conflicts are not being handled properly. When a class name shadows or conflicts with variables accessed from outer scopes, the bundler doesn't prevent the name collision as expected.

### Reproduction

```js
const MyClass = 1;

{
  class MyClass {
    method() {
      return MyClass; // Should reference the class, but name collision occurs
    }
  }
  
  const instance = new MyClass();
  console.log(instance.method());
}
```

The class name `MyClass` conflicts with the outer variable `MyClass`, but the name isn't being properly reserved/forbidden for the outer variable. This can lead to incorrect code generation where variable names collide.

### Expected behavior

The bundler should detect when a class declaration's name conflicts with variables from outer scopes that are accessed within the class scope, and rename those outer variables to avoid collisions during code generation.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
