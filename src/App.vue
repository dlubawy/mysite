<template>
  <div id="app" class="d-flex flex-column">
    <Navbar />
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";

export default {
  name: "App",
  components: {
    Navbar,
  },
};
</script>

<style>
#app {
  height: 100vh;
}
</style>
