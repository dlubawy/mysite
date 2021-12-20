import Vue from "vue";
import App from "./App.vue";

import "bootstrap";
import "bootswatch/dist/sandstone/bootstrap.min.css";

import { auth } from "./firebaseConfig.js";
import { signInAnonymously } from "firebase/auth";

Vue.config.productionTip = false;

signInAnonymously(auth);

new Vue({
  render: (h) => h(App),
}).$mount("#app");
