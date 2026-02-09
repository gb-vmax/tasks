# Bug Report

### Describe the bug

After a recent update, I'm getting errors when working with cookie jars. The application crashes when trying to interact with cookies, and I'm seeing `TypeError: Cannot read properties of null` in the console.

### Reproduction

```js
// Create a new cookie jar
const jar = cookieJar.init();

// Try to access or manipulate cookies
jar.cookies.push(newCookie); // TypeError: Cannot read properties of null (reading 'push')

// Even checking length fails
console.log(jar.cookies.length); // TypeError: Cannot read properties of null (reading 'length')
```

### Expected behavior

When initializing a new cookie jar, the `cookies` property should be an empty array that can be manipulated with standard array methods like `push`, `splice`, etc.

The jar should be initialized with:
```js
{
  name: 'Default Jar',
  cookies: []  // Should be an empty array, not null
}
```

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking my workflow as I can't add or manage cookies anymore. Any code that tries to iterate over or modify the cookies array fails immediately.

---
Repository: /testbed
