<template>
  <form role="form" v-on:submit.prevent="send">
    <div class="container">
      <div class="row required">
        <label for="name" class="control-label">Name</label>
        <input
          type="text"
          class="form-control"
          name="name"
          placeholder="Jane Doe"
          required="true"
          v-model="name"
        />
      </div>
      <div class="row required">
        <label for="email" class="control-label">Email</label>
        <input
          type="email"
          class="form-control"
          name="email"
          placeholder="jdoe@example.com"
          required="true"
          v-model="email"
        />
      </div>
      <div class="row">
        <label for="message" class="control-label">Message</label>
        <textarea
          v-model="message"
          class="form-control"
          rows="5"
          name="message"
          title="message"
          placeholder="Message text"
        ></textarea>
      </div>
      <div class="row-2 pt-3">
        <input class="btn btn-primary" type="submit" value="Submit" />
      </div>
    </div>
  </form>
</template>

<script>
export default {
  name: "ContactForm",
  data() {
    return {
      name: "",
      email: "",
      message: "",
    };
  },
  methods: {
    send() {
      console.log(`${this.name} - ${this.email}\n\n${this.message}`);
    },
  },
};
</script>

<style></style>
