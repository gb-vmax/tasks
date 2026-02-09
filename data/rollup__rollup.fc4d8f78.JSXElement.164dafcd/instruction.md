# Bug Report

### Describe the bug

I'm experiencing an issue with JSX attribute rendering when using spread attributes followed by regular attributes. The attributes after a spread don't seem to be getting wrapped in an object correctly, which is causing syntax errors in the generated output.

### Reproduction

```jsx
const Component = () => {
  return (
    <div {...props} className="test" id="main">
      Content
    </div>
  );
};
```

When I have a spread attribute followed by multiple regular attributes, the second attribute onwards are not being properly grouped into an object. The generated code appears to be malformed.

### Expected behavior

All attributes after a spread should be properly wrapped in an object literal so the output is valid JavaScript. Something like:

```js
createElement('div', { ...props, className: "test", id: "main" }, 'Content')
```

### Additional context

This seems to happen specifically when:
1. Using JSX automatic mode
2. Have a spread attribute 
3. Followed by two or more regular attributes

The first attribute after the spread works fine, but subsequent ones break the object literal structure.

---
Repository: /testbed
