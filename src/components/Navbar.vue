<template>
  <ul class="nav nav-pills">
    <li class="nav-item">
      <a
        v-on:click="updateTab('home')"
        v-bind:class="getTabClass('home')"
        href="#home"
        >Home</a
      >
    </li>
    <li class="nav-item">
      <a
        v-on:click="updateTab('about')"
        v-bind:class="getTabClass('about')"
        href="#about"
        >About</a
      >
    </li>
    <li class="nav-item">
      <a
        v-on:click="updateTab('skills')"
        v-bind:class="getTabClass('skills')"
        href="#skills"
        >Skills</a
      >
    </li>
    <li class="nav-item">
      <a
        v-on:click="updateTab('contact')"
        v-bind:class="getTabClass('contact')"
        href="#contact"
        >Contact</a
      >
    </li>
  </ul>
</template>

<script>
var tag = document.URL.split("#")[1];
if (tag == null) {
  tag = "home";
}

export default {
  name: "Navbar",
  data() {
    return {
      currentTab: tag,
    };
  },
  methods: {
    getTabClass(id) {
      const linkClass = "nav-link";
      if (this.currentTab == id) {
        return linkClass + " active";
      }
      return linkClass;
    },
    updateTab(id) {
      this.currentTab = id;
    },
  },
};
</script>

<style></style>
