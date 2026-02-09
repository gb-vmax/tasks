# Bug Report

### Describe the bug

After a recent update, I'm getting an error when trying to modify state returned from `getState()`. It seems like the state object is being frozen, which prevents any direct modifications.

### Reproduction

```js
const store = createStore({ count: 0, user: { name: 'test' } });

const state = store.getState();
state.count = 5; // TypeError: Cannot assign to read only property 'count'
```

Also noticing that if my state object has a `lastAccessed` property, it gets set to `null` unexpectedly:

```js
const store = createStore({ 
  data: 'value',
  lastAccessed: Date.now() 
});

console.log(store.getState().lastAccessed); // null instead of the timestamp
```

### Expected behavior

`getState()` should return the current state object that can be used normally. If the state contains a `lastAccessed` property, it should preserve its value.

### System Info
- @mantine/store version: latest
- Node version: 18.x

---
Repository: /testbed
