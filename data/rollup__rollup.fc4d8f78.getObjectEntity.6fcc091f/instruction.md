# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when working with function prototypes in my code. The bundler hangs and eventually crashes with a stack overflow error when processing certain function declarations.

### Reproduction

```js
function MyConstructor() {
  this.value = 42;
}

MyConstructor.prototype.method = function() {
  return this.value;
};

const instance = new MyConstructor();
console.log(instance.method());
```

When bundling code like this, the process gets stuck in an infinite loop and never completes. The CPU usage spikes to 100% and the build never finishes.

### Expected behavior

The bundler should process function prototypes without hanging. The code should bundle successfully and the output should work as expected.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have started recently - the same code was working fine in previous versions. Any help would be appreciated!

---
Repository: /testbed
