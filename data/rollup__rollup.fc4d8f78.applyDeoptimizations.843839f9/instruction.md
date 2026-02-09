# Bug Report

### Describe the bug

I'm encountering an issue with class declarations where variable names are being incorrectly forbidden during bundling. When a class is declared and variables with the same name exist in outer scopes, the bundler is applying name restrictions to the wrong variables.

### Reproduction

```js
class MyClass {
  constructor() {
    const MyClass = 'inner';
    console.log(MyClass);
  }
}

const MyClass = 'outer';
export { MyClass };
```

When bundling this code, the outer `MyClass` variable gets its name forbidden even though it should be allowed to keep its name. The class's own variable should be the one with naming restrictions applied.

### Expected behavior

The bundler should correctly identify which variables need name restrictions based on the class declaration. Variables outside the class scope that happen to share the same name as the class should not have their names forbidden unless they are actually the class variable itself.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
