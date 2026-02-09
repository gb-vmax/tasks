# Bug Report

### Middleware execution order reversed

I'm experiencing an issue where middleware functions are being executed in the wrong order. When I add multiple middleware using `.use()`, they seem to run in reverse order from how I added them.

### Reproduction
```js
const pipeline = trough()
  .use((value, next) => {
    console.log('First middleware')
    next(null, value)
  })
  .use((value, next) => {
    console.log('Second middleware')
    next(null, value)
  })
  .use((value, next) => {
    console.log('Third middleware')
    next(null, value)
  })

pipeline.run('test')
```

### Expected behavior
The middleware should execute in the order they were added:
```
First middleware
Second middleware
Third middleware
```

### Actual behavior
They execute in reverse order:
```
Third middleware
Second middleware
First middleware
```

This is breaking my processing pipeline where order matters. Is this intentional or a bug?

---
Repository: /testbed
