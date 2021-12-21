import Vue from "vue";
import App from "./App.vue";

import "bootstrap";
import "bootswatch/dist/sandstone/bootstrap.min.css";

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
}).$mount("#app");
