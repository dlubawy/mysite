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
      <div class="row required">
        <label for="subject" class="control-label">Subject</label>
        <input
          type="text"
          class="form-control"
          name="subject"
          placeholder="Subject"
          required="true"
          v-model="subject"
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
import { analytics, db } from "../firebaseConfig.js";
import { collection, addDoc } from "firebase/firestore";
import { logEvent } from "firebase/analytics";

export default {
  name: "ContactForm",
  data() {
    return {
      name: "",
      email: "",
      subject: "",
      message: "",
    };
  },
  props: {
    user: String,
  },
  methods: {
    send() {
      if (this.user != null) {
        addDoc(collection(db, "mail"), {
          toUids: ["0GHgDhqf3AmfYXVfSaiE"],
          message: {
            subject: this.subject,
            text: `Name: ${this.name}\nEmail: ${this.email}\n\n${this.message}`,
            html: `<span>Name: ${this.name}</span><br/><span>Email: ${this.email}</span><br/><p>${this.message}</p>`,
          },
        }).then(() => {
          alert("Message sent!");
          logEvent(analytics, "select_content", {
            content_type: "form",
            item_id: "email",
          });
        });
      } else {
        alert("Message rejected.");
      }
    },
  },
};
</script>

<style></style>
