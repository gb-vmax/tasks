# Bug Report

### Describe the bug

There's a syntax error in the response.ts file that's breaking the build. It looks like some code got accidentally inserted in the middle of an object literal definition.

### Reproduction

The issue is in the `packages/insomnia-sdk/src/objects/response.ts` file around line 258. When trying to build or use the SDK, you'll encounter a syntax error because there's a function definition (`const haveJsonBody = ...`) that's been placed inside an object literal where it shouldn't be.

The problematic section has:
```js
body: (expected: string) => haveBody(expected, false),
const haveJsonBody = (expected: object, checkEquality: boolean) => verify(this.json(), expected, checkEquality);

jsonBody: (expected: object) => haveJsonBody(expected, false),
```

This causes the parser to fail since you can't have a `const` declaration in the middle of object properties.

### Expected behavior

The file should compile without syntax errors and the SDK should be usable.

### System Info
- Insomnia SDK version: latest
- Node version: any

---
Repository: /testbed
