# Bug Report

### Describe the bug

I'm experiencing an issue with tagged template expressions where the template literal parts are being incorrectly passed to the tag function instead of the expression values.

### Reproduction

```js
const myTag = (strings, ...values) => {
  console.log('strings:', strings);
  console.log('values:', values);
  return strings.reduce((result, str, i) => 
    result + str + (values[i] || ''), ''
  );
};

const name = 'World';
const greeting = myTag`Hello ${name}!`;
```

### Expected behavior

The tag function should receive:
- `strings`: An array of the static string parts (e.g., `['Hello ', '!']`)
- `values`: The interpolated expression values (e.g., `['World']`)

However, it seems like the static template parts (quasis) are being passed where the expression values should be, causing the tag function to receive incorrect arguments.

### Additional context

This appears to affect how tagged template expressions interact with member expressions as well. The condition for determining when to include the object reference seems inverted.

---
Repository: /testbed
