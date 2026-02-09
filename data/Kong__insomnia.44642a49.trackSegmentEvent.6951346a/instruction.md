# Bug Report

### Describe the bug

After a recent update, the test setup file appears to have a syntax error that's breaking the application. The `global.main` object configuration seems to be malformed - there are function definitions that appear before the object property assignment syntax is complete.

### Reproduction

Looking at the setup file, the structure looks like:

```js
global.main = {
global.main.getTrackedEvents = (eventName) => {
  // ... function body
};

global.main.clearTrackedEvents = () => {
  // ... function body  
};

global.main.configureSegmentTracking = (config) => {
  // ... function body
};

 trackSegmentEvent: (...args) => {
   // ... function body
 }
  trackPageView: () => { },
};
```

The issue is that `global.main.getTrackedEvents`, `global.main.clearTrackedEvents`, and `global.main.configureSegmentTracking` are being defined as standalone assignments outside of the object literal, but they appear inside what should be the object literal definition that starts with `global.main = {`.

### Expected behavior

The code should be syntactically valid JavaScript. Either these should be proper object properties within the literal, or they should be defined after the object is created.

### System Info
- Node version: Latest
- Package: insomnia

This is preventing the application from starting up correctly. Any help would be appreciated!

---
Repository: /testbed
