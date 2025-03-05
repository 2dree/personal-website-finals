// 1. Initialize Vue App
import { createApp } from 'vue';
import App from './App.vue';
import './assets/style.css'; // Custom styling

const app = createApp(App);
app.mount('#app');

// 2. W3.CSS Parallax Template Integration (inside App.vue)
<template>
  <div>
    <nav class="w3-top w3-bar w3-white w3-padding w3-card w3-wide">
      <a href="#home" class="w3-bar-item w3-button w3-wide"><b>LOGO</b></a>
      <div class="w3-left">
        <a href="#home" class="w3-bar-item w3-button w3-hover-opacity">HOME</a>
        <a href="#about" class="w3-bar-item w3-button w3-hover-opacity">ABOUT</a>
        <a href="#portfolio" class="w3-bar-item w3-button w3-hover-opacity">PORTFOLIO</a>
        <a href="#contact" class="w3-bar-item w3-button w3-hover-opacity">CONTACT</a>
      </div>
    </nav>

    <header class="w3-display-container w3-wide" id="home" style="width:100vw; height:100vh; overflow:hidden; position:relative;">
      <div class="bgimg-1 w3-display-container w3-opacity-min" id="home">
  <div class="w3-display-middle" style="white-space:nowrap;">
    <span class="w3-center w3-padding-large w3-black w3-xlarge w3-wide w3-animate-opacity">MY <span class="w3-hide-small">PERSONAL</span> WEBSITE</span>
  </div>
</div>
    
    </header>

    <section class="w3-container w3-padding-64" id="about">
      <h2 class="w3-center">About Me</h2>
      <div class="w3-row w3-padding-32">
        <div class="w3-col m12 w3-padding">
          <p class="w3-center"><em>I love photography</em></p>
          <p>We have created a fictional "personal" website/blog, and our fictional character is a hobby photographer. 
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        </div>
        <div class="w3-col m6 w3-padding">
          <img src="https://scontent.fmnl4-7.fna.fbcdn.net/v/t1.15752-9/467319362_1146429103744083_6208177518650473317_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=9f807c&_nc_ohc=PLbmxFGCNgIQ7kNvgFXKjBq&_nc_oc=AdhDd_3Pp9Fl_nyVQT0hlZkrzyiHTNIoD_t82HOAe_qofehP9ZTGq9cB8Fi-S8DsL6k&_nc_zt=23&_nc_ht=scontent.fmnl4-7.fna&oh=03_Q7cD1gEpSB03P1clk1x4ykFRMCFmlW6fQ-TWKb-tO1vfT2ZrDA&oe=67EF9CF9" 
          alt="About Me Image" style="width:100%; 
          border-radius:10px;">
        </div>
        <div class="w3-col m6 w3-padding">
          <p>Welcome to my website. I am lorem ipsum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        </div>
      </div>
      <div class="w3-container w3-padding-32">
        <h3 class="w3-center">Here are some of my skills:</h3>
        
       <p style="text-align: left;" p class="w3-wide"><i class="fa fa-camera"></i>Photography</p>
          <div class="w3-light-grey">
          <div class="w3-container w3-padding-small w3-dark-grey w3-center" style="width:90%">90%</div>
          </div>
      <br>
        
       <p style="text-align: left;" p class="w3-wide"><i class="fa fa-laptop"></i>Web Design</p>
          <div class="w3-light-grey">
          <div class="w3-container w3-padding-small w3-dark-grey w3-center" style="width:85%">85%</div>
          </div>
      <br>

        <p style="text-align: left;" p class="w3-wide"><i class="fa fa-photo"></i>Photoshop</p>
        <div class="w3-light-grey">
        <div class="w3-container w3-padding-small w3-dark-grey w3-center" style="width:75%">75%</div>
        </div>
        </div>
    </section>

    <div class="w3-row w3-center w3-dark-grey w3-padding-16">
  <div class="w3-quarter w3-section">
    <span class="w3-xlarge">14+</span><br>
    Partners
  </div>
  <div class="w3-quarter w3-section">
    <span class="w3-xlarge">55+</span><br>
    Projects Done
  </div>
  <div class="w3-quarter w3-section">
    <span class="w3-xlarge">89+</span><br>
    Happy Clients
  </div>
  <div class="w3-quarter w3-section">
    <span class="w3-xlarge">150+</span><br>
    Meetings
  </div>
</div>

<!-- Second Parallax Image with Portfolio Text -->
<div class="bgimg-2 w3-display-container w3-opacity-min">
  <div class="w3-display-middle">
    <span class="w3-xxlarge w3-text-white w3-wide">MY GALLERY</span>
  </div>
</div>


<!-- Container (Portfolio Section) -->
<div class="w3-content w3-container w3-padding-64" id="portfolio">
  <h3 class="w3-center">PHOTOS</h3>
  <p class="w3-center"><em>Here are some of my Photo Gallery Dump.<br> Too random</em></p><br>
</div>



<!-- Responsive Grid. Four columns on tablets, laptops and desktops. Will stack on mobile devices/small screens (100% width) -->
<div class="w3-row-padding w3-center">
    <div class="w3-col m3">
      <img src="https://scontent.fmnl4-2.fna.fbcdn.net/v/t1.15752-9/481904531_645654731162380_5552048263239859323_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=9f807c&_nc_ohc=MpKJpjGU7NoQ7kNvgF-CtFf&_nc_oc=Adg2UpHbl_s67dsfQ-BPkxlbbXla8OhYt-5AVWAlqDH8yes00sZT-Ruz94Z7KsNdBWw&_nc_zt=23&_nc_ht=scontent.fmnl4-2.fna&oh=03_Q7cD1gGO61hWog8VRlmddu2fodDHDHMfqW5lJmTSKOlCLgnAlw&oe=67EFA0D2" 
      style="width:100%" class="w3-hover-opacity" alt="Potcor x starbs?">
    </div>

    <div class="w3-col m3">
      <img src="https://scontent.fmnl4-7.fna.fbcdn.net/v/t1.15752-9/482148352_1004765961551815_3650695014809342931_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=9f807c&_nc_ohc=CV_DFUH-CesQ7kNvgEFpr7m&_nc_oc=AdgOku1D1jpLx9_loJhUcthpeQxcwwL23zii1UsXU-CaGdq-QOQA6SRQosmARuGLS_s&_nc_zt=23&_nc_ht=scontent.fmnl4-7.fna&oh=03_Q7cD1gHikIrG8yNivvpExuaAMaTGc9VGJ1d9asDZqeB9zLEUZQ&oe=67EF98B3" 
      style="width:100%" class="w3-hover-opacity" alt="Nanyang">
    </div>

    <div class="w3-col m3">
      <img src="https://scontent.fmnl4-4.fna.fbcdn.net/v/t1.15752-9/481978343_497002893264923_3668156600164171348_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=9f807c&_nc_ohc=I0Und6z8sakQ7kNvgF31nac&_nc_oc=AdjxJ0Mobklt0Usf0dk7TjBKzOYudZ2iDuIDZdrZwwtNOsKyrZ2sMLeJNeC5akNJQ2A&_nc_zt=23&_nc_ht=scontent.fmnl4-4.fna&oh=03_Q7cD1gFRPhlDYJZZYYJS44lNu7K6bVDfta54iI8AjhW37mU6VA&oe=67EFD4EA" 
      style="width:100%" class="w3-hover-opacity" alt="Boat House?">
    </div>

    <div class="w3-col m3">
      <img src="https://scontent.fmnl4-2.fna.fbcdn.net/v/t1.15752-9/482292757_1159591921958639_3012151894625487496_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=9f807c&_nc_ohc=tIOdvbptA6wQ7kNvgHxYBqS&_nc_oc=AdhftMvzD-B_JJ2jdppm6u14kUbKUSh8ju0Cyek0cHMVq6Tzpq8nqZqS-LCqE9GPLi8&_nc_zt=23&_nc_ht=scontent.fmnl4-2.fna&oh=03_Q7cD1gE45b2BKTj5M4Ybd_tU1Jx2NH3wnooxlICREoHcquGTRg&oe=67EFD19F" 
      style="width:100%" class="w3-hover-opacity" alt="Quiet ocean">
    </div>
  </div>

  <div class="w3-row-padding w3-center w3-section">
    <div class="w3-col m3">
      <img src="https://scontent.fmnl4-4.fna.fbcdn.net/v/t1.15752-9/481808341_1179266047200039_707161907799634328_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=9f807c&_nc_ohc=FqC9UNdRgqMQ7kNvgEeFRuL&_nc_oc=AdhFfAq7BPzWpBPeUYl5c6cuNixIJ7no98gKixbqifQlmj6gEG7bCFOn2JS6VZJTjWA&_nc_zt=23&_nc_ht=scontent.fmnl4-4.fna&oh=03_Q7cD1gGDMnBUvQoPSowiqaOVinadTBG3_EgUefgOMWle8ifIGQ&oe=67EFD2B3" 
      style="width:100%" class="w3-hover-opacity" alt="Niki">
    </div>

    <div class="w3-col m3">
      <img src="https://scontent.fmnl4-1.fna.fbcdn.net/v/t1.15752-9/482147584_1316119556381501_7837411078638539732_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=9f807c&_nc_ohc=tPU-J9LpB94Q7kNvgGpweO1&_nc_oc=Adi3G6veVsgPcqtB3eBSuUxIMBl_tTu-fu4lAVcVZPBqZaCWdbI86FX0a_PPnKgaME0&_nc_zt=23&_nc_ht=scontent.fmnl4-1.fna&oh=03_Q7cD1gGxDfsNsV770KaOXF5mKziQO7oiMJWMwO_FfC9as6H3Fw&oe=67EFA77A" 
      style="width:100%"  class="w3-hover-opacity" alt="mcdo?">
    </div>

    <div class="w3-col m3">
      <img src="https://scontent.fmnl4-2.fna.fbcdn.net/v/t1.15752-9/481901244_645946974513115_4659766834960010463_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=9f807c&_nc_ohc=uf6AiItJyc4Q7kNvgFGFbVv&_nc_oc=AdgBHcJQvpldtNAamtwWSbuWQ-gOHR48TBCeNHWlg3TNaOdV8xnSsWTqCbXJLKb38qY&_nc_zt=23&_nc_ht=scontent.fmnl4-2.fna&oh=03_Q7cD1gEdivszip-GG0Ypx32cEnN5LWWRWipHbbsm0coxbI2_cQ&oe=67EFBA4F" 
      style="width:100%"  class="w3-hover-opacity" alt="F1">
    </div>

    <div class="w3-col m3">
      <img src="https://scontent.fmnl4-6.fna.fbcdn.net/v/t1.15752-9/481517309_938179091816620_8936053091630437504_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=9f807c&_nc_ohc=5LYnrSaAyeIQ7kNvgEeiHXc&_nc_oc=Adi0nheILQkWleSrnkj5Px3UIIrL9Sxy5VK4cjG1K3-RkQ5ZcnprtWXoNqsk_asGVi4&_nc_zt=23&_nc_ht=scontent.fmnl4-6.fna&oh=03_Q7cD1gH8Vi-7upOB5gHjfRyBP6YM3VqjDdiX03t9ZRM8c6-MWg&oe=67EFBF2E" 
      style="width:100%" class="w3-hover-opacity" alt="Sailing">
    </div>
    <button class="w3-button w3-padding-large w3-light-grey" style="margin-top:64px">LOAD MORE</button>
  </div>
</div>


<!-- Third Parallax Image with Portfolio Text -->
<div class="bgimg-3 w3-display-container w3-opacity-min">
  <div class="w3-display-middle">
     <span class="w3-xxlarge w3-text-white w3-wide">CONTACT</span>
  </div>
</div>
 

<!-- Container (Contact Section) -->
<div class="w3-content w3-container w3-padding-64" id="contact">
  <h3 class="w3-center">WHERE I WORK</h3>
  <p class="w3-center"><em>I'd love your feedback!</em></p>

  <div class="w3-row w3-padding-32 w3-section">
    <div class="w3-col m4 w3-container">
      <img src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/e3/48/e5/river-park.jpg?w=1200&h=-1&s=1" class="w3-image w3-round" style="width:100%">
    </div>
    <div class="w3-col m8 w3-panel">
      <div class="w3-large w3-margin-bottom">
        <i class="fa fa-map-marker fa-fw w3-hover-text-black w3-xlarge w3-margin-right"></i> Chicago, US<br>
        <i class="fa fa-phone fa-fw w3-hover-text-black w3-xlarge w3-margin-right"></i> Phone: +00 151515<br>
        <i class="fa fa-envelope fa-fw w3-hover-text-black w3-xlarge w3-margin-right"></i> Email: mail@mail.com<br>
      </div>
      <p>Swing by for a cup of <i class="fa fa-coffee"></i>, or leave me a note:</p>

      <!-- Vue.js Form -->
      <form @submit.prevent="submitComment">
        <div class="w3-row-padding" style="margin:0 -16px 8px -16px">
          <div class="w3-half">
            <input v-model="newComment.name" class="w3-input w3-border" type="text" placeholder="Name" required>
          </div>
        </div>
        <input v-model="newComment.message" class="w3-input w3-border" type="text" placeholder="Message" required>
        <button class="w3-button w3-black w3-right w3-section" type="submit">
          <i class="fa fa-paper-plane"></i> SEND MESSAGE
        </button>
      </form>

      <!-- Display Comments --> 
    <div>
    <h4>Comments:</h4>
    <ul class="my-comment-list">
  <li v-for="comment in comments" :key="comment.id">
    <strong>{{ comment.name }}</strong>: {{ comment.message }}
  </li>
</ul>
    </div>
  </div>
</div>
</div>
<!-- Footer -->
<footer class="w3-center w3-black w3-padding-64 w3-opacity w3-hover-opacity-off">
  <a href="#home" class="w3-button w3-light-grey"><i class="fa fa-arrow-up w3-margin-right"></i>To the top</a>
  <div class="w3-xlarge w3-section">
    <i class="fa fa-facebook-official w3-hover-opacity"></i>
    <i class="fa fa-instagram w3-hover-opacity"></i>
    <i class="fa fa-snapchat w3-hover-opacity"></i>
    <i class="fa fa-pinterest-p w3-hover-opacity"></i>
    <i class="fa fa-twitter w3-hover-opacity"></i>
    <i class="fa fa-linkedin w3-hover-opacity"></i>
  </div>
  <p>Powered by <a href="https://www.w3schools.com/w3css/default.asp" title="W3.CSS" target="_blank" class="w3-hover-text-green">w3.css</a></p>
</footer>



</template>

<script>
import { createClient } from "@supabase/supabase-js";

const supabase = createClient(
  "https://glvqdlzsvdmvplohpmgq.supabase.co", 
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdsdnFkbHpzdmRtdnBsb2hwbWdxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDExNjAxNTYsImV4cCI6MjA1NjczNjE1Nn0.UauGe2SIarphoWwwAHweqDdV13wkK1k1lSgfFSjW0lc"
);

export default {
  data() {
    return {
      comments: [], // List of comments fetched from Supabase
      newComment: { name: "", message: "" } // Use an object for the new comment data
    };
  },
  methods: {
    async fetchComments() {
      try {
        const { data, error } = await supabase.from("comments").select("*");

        if (error) throw error; // Handle any errors

        console.log("Fetched data from Supabase:", data);
        this.comments = Array.isArray(data) ? data : [];
      } catch (err) {
        console.error("Error fetching comments:", err.message);
      }
    },

    async submitComment() {
      // Validate that both name and message have values
      if (!this.newComment.name.trim() || !this.newComment.message.trim()) {
        console.error("Both Name and Message are required!");
        return;
      }

      // Insert the comment into Supabase
      const { error } = await supabase
        .from("comments")
        .insert([{ name: this.newComment.name, message: this.newComment.message }]);

      if (error) {
        console.error("Error inserting comment:", error.message);
        return;
      }

      console.log("Comment added successfully!");

      await this.fetchComments(); // Refresh the comments list

      // Reset the newComment object so it's ready for the next input
      this.newComment = { name: "", message: "" };
    }
  },
  mounted() {
    this.fetchComments(); // Load comments when the component is mounted
  }
};
</script>

<style scoped>
  .my-comment-list {
    list-style: none !important;
    padding: 0 !important;
    margin: 0 !important;
    text-align: left !important;
  }
  .my-comment-list li {
    display: block;
    margin: 0.5rem 0 !important;
    text-align: left !important;
  }
</style>
