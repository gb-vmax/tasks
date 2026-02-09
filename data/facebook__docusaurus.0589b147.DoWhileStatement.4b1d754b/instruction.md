# Bug Report

### Describe the bug

I'm experiencing an issue where `do-while` loops are not being generated correctly in the output. Instead of producing valid JavaScript code, the generator seems to be outputting literal text that includes placeholders like `<body>` and `<test>`.

### Reproduction

```js
// Input MDX/JavaScript with a do-while loop
const code = `
function example() {
  let i = 0;
  do {
    console.log(i);
    i++;
  } while (i < 5);
}
`;

// After processing, the output contains:
// "do <body> while (<test>);"
// instead of the actual do-while statement
```

### Expected behavior

The generator should produce valid JavaScript code with properly formatted `do-while` statements, like:
```js
do {
  console.log(i);
  i++;
} while (i < 5);
```

Instead, it's outputting malformed code with literal placeholder text.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
