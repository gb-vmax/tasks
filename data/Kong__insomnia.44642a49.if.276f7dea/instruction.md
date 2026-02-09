# Bug Report

### Describe the bug

I'm experiencing an issue with the `withDescendants` function after a recent update. It looks like there's duplicate code in the function definition - the function signature and implementation appear twice, which is causing syntax errors when trying to build the project.

### Reproduction

The issue is in `packages/insomnia/src/common/database.ts` in the `withDescendants` method. When I try to use this function:

```js
const descendants = await database.withDescendants(parentDoc);
```

The application fails to compile/run due to malformed code in the database module.

### Expected behavior

The `withDescendants` function should have a single, valid implementation and execute without syntax errors. It should return all descendant documents as before.

### Additional context

Looking at the source code, it appears that the function definition starts twice - once with the new signature including `maxDepth` parameter, and again with the old implementation. This creates invalid JavaScript/TypeScript syntax.

The build process fails immediately when trying to import or use anything from the database module.

---
Repository: /testbed
