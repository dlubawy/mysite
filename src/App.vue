<template>
  <div id="app">
    <Navbar />
    <div class="d-flex flex-column text-white">
      <div id="home">
        <div id="background-image" class="bg-image">
          <br />
          <div
            id="home-text"
            class="row align-items-center mx-auto text-center h-100 text-white"
          >
            <div class="col">
              <h1>Andrew Lubawy</h1>
              <p class="lead">B.S. Electrical Engineering</p>
            </div>
            <div>
              <a href="#about" class="btn btn-link hvr-grow">
                <img src="./assets/down_arrow.png" alt="Down arrow icon" />
              </a>
            </div>
          </div>
        </div>
      </div>
      <div id="about">
        <br />
        <div class="container text-center">
          <div class="row gap-2">
            <div class="col-md-4 m-auto">
              <div class="container">
                <img
                  src="./assets/profile.webp"
                  class="img-fluid rounded-circle"
                  alt="Profile picture of Andrew"
                />
              </div>
            </div>
            <div class="col m-auto">
              <h2>Hello! I'm Andrew Lubawy.</h2>
              <p class="lead">
                Data Engineer for Cue Health. Ex-NASA contractor. Tech
                entusiast. I enjoy taking things apart and learning what makes
                them tick. I also enjoy creating things, so if you need
                something, I'll happily try and build it for you.
              </p>
            </div>
          </div>
        </div>
        <br />
      </div>
      <div id="skills">
        <br />
        <div class="container text-center">
          <div class="row">
            <h2>Skills</h2>
          </div>
          <br />
          <div class="row gap-4">
            <div class="col">
              <img
                src="./assets/embedded.webp"
                class="rounded"
                width="200"
                height="200"
                alt="Picture of microcontrollers"
              />
              <p class="lead">
                Embedded systems design with hardware programming knowledge in C
                and Verilog HDL.
              </p>
            </div>
            <div class="col">
              <img
                src="./assets/full_stack.webp"
                class="rounded"
                width="200"
                height="200"
                alt="Stack of pancakes"
              />
              <p class="lead">
                Full stack development. Backend programming with Django, Rails,
                and Flask. Frontend programming with JavaScript, HTML, and CSS.
              </p>
            </div>
            <div class="col">
              <img
                src="./assets/circuit.webp"
                class="rounded"
                width="200"
                height="200"
                alt="Printed circuit board"
              />
              <p class="lead">
                Circuit design and debugging. Experience with soldering,
                oscilloscopes, multimeters, and Altium Designer for PCB design.
              </p>
            </div>
            <div class="col">
              <img
                src="./assets/code.webp"
                class="rounded"
                width="200"
                height="200"
                alt="Lines of code"
              />
              <p class="lead">
                Software development and object oriented language proficiency
                with Python, Java, C++, and Ruby.
              </p>
            </div>
            <div class="col">
              <img
                src="./assets/pipes.webp"
                class="rounded"
                width="200"
                height="200"
                alt="Pipes"
              />
              <p class="lead">
                Data engineering using SQL, BigQuery, and dbt. Experience with
                creating custom data pipelines using Python and GCP.
              </p>
            </div>
          </div>
        </div>
        <br />
      </div>
      <div id="contact">
        <br />
        <div class="container text-center gap-4">
          <div class="row">
            <h2>Contact Me</h2>
          </div>
          <div class="row">
            <ContactForm :user="user" />
          </div>
        </div>
        <br />
      </div>
      <footer class="footer bg-primary">
        <br />
        <div class="container text-center">
          <div class="row-2 justify-content-center">
            <div class="btn-group">
              <a
                type="button"
                class="btn btn-link"
                href="https://github.com/dlubawy"
                target="_blank"
                rel="noreferrer"
                v-on:click="logClick('GitHub')"
              >
                <img
                  src="./assets/github_icon.png"
                  class="img-fluid"
                  alt="GitHub icon"
                />
              </a>
              <a
                type="button"
                class="btn btn-link"
                href="https://www.linkedin.com/in/andrewlubawy"
                target="_blank"
                rel="noreferrer"
                v-on:click="logClick('LinkedIn')"
              >
                <img
                  src="./assets/linkedin_icon.png"
                  class="img-fluid"
                  alt="LinkedIn icon"
                />
              </a>
            </div>
          </div>
          <div class="row">
            <p class="small text-muted">Site built by myself.</p>
          </div>
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import ContactForm from "./components/ContactForm.vue";

import { auth, analytics } from "./firebaseConfig.js";
import { logEvent } from "firebase/analytics";
import { signInAnonymously } from "firebase/auth";

signInAnonymously(auth);

var tag = document.URL.split("#")[1];
if (tag == null) {
  tag = "home";
}

export default {
  name: "App",
  data() {
    return {
      user: null,
    };
  },
  components: {
    Navbar,
    ContactForm,
  },
  methods: {
    logClick(id) {
      logEvent(analytics, "select_content", {
        content_type: "link",
        item_id: id,
      });
    },
  },
  created() {
    auth.onAuthStateChanged((user) => {
      if (user) {
        this.user = user;
      }
    });
  },
};
</script>

<style>
#app {
  height: 100vh;
  position: relative;
}
#background-image {
  background-image: url("./assets/background.webp");
  height: 100vh;
  background-size: cover;
}
#home-text {
  max-width: 42em;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
}
#about {
  background-color: #81633e;
}
#skills {
  background-color: #2b5b43;
}
#contact {
  background-color: #2a4352;
}
</style>
