# MySite

## About

This is my personal website which I built after being convinced to buy my
name's domain name. Figured it shouldn't stay empty. Very basic, built it from
[Bootstrap](http://getbootstrap.com/) then expanded to using ~~Flask~~ [Vue.js](https://vuejs.org/) and
[Firebase](https://firebase.google.com/) when I exceeded the scope of a static website
with my contact form. I moved from Flask to Vue.js and Firebase to explore
server-less deployments and because Firebase is a free hosting (or at least very cheap)
hosting solution which allows TLS hosting.

## Usage

### Configuration

Replace the Firebase configuration in `src/firebaseConfig.js` to your own
before use.

### Project setup

```
npm install
```

#### Compiles, hot-reloads, and starts Firebase emulators

```
npm run serve
```

#### Compiles and minifies for production

```
npm run build
```

#### Lints and fixes files

```
npm run lint
```

#### Builds and deploys to Firebase

```
npm run deploy
```

#### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).
