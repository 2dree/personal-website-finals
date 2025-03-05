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
      <img class="w3-image" src="https://storage.googleapis.com/pod_public/750/215988.jpg" alt="Parallax Image" style="width:100%; height:100vh; object-fit:cover; position:absolute; top:0; left:0;">
      <div class="w3-display-middle w3-text-white w3-center w3-container">
        <h1 class="w3-jumbo w3-hide-small"><b>My Personal Website</b></h1>
        <h2 class="w3-hide-large w3-hide-medium"><b>My Personal Website</b></h2>
        <p class="w3-large">A creative space to showcase my work</p>
      </div>
    </header>

    <section class="w3-container w3-padding-64" id="about">
      <h2 class="w3-center">About Me</h2>
      <div class="w3-row w3-center w3-padding-32">
        <div class="w3-col m6 w3-padding">
          <img src="https://scontent.fmnl4-7.fna.fbcdn.net/v/t1.15752-9/467319362_1146429103744083_6208177518650473317_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=9f807c&_nc_ohc=PLbmxFGCNgIQ7kNvgFXKjBq&_nc_oc=AdhDd_3Pp9Fl_nyVQT0hlZkrzyiHTNIoD_t82HOAe_qofehP9ZTGq9cB8Fi-S8DsL6k&_nc_zt=23&_nc_ht=scontent.fmnl4-7.fna&oh=03_Q7cD1gEpSB03P1clk1x4ykFRMCFmlW6fQ-TWKb-tO1vfT2ZrDA&oe=67EF9CF9" alt="About Me Image" style="width:100%; border-radius:10px;">
        </div>
        <div class="w3-col m6 w3-padding">
          <p class="w3-center"><em>I love photography</em></p>
          <p>We have created a fictional "personal" website/blog, and our fictional character is a hobby photographer. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        </div>
      </div>
      <div class="w3-container w3-padding-32">
        <h3 class="w3-center">Here are some of my skills:</h3>
        <div class="w3-light-grey w3-round-xlarge w3-small">
          <div class="w3-container w3-dark-grey w3-round-xlarge w3-padding" style="width:90%">Photography 90%</div>
        </div>
        <br>
        <div class="w3-light-grey w3-round-xlarge w3-small">
          <div class="w3-container w3-dark-grey w3-round-xlarge w3-padding" style="width:85%">Web Design 85%</div>
        </div>
        <br>
        <div class="w3-light-grey w3-round-xlarge w3-small">
          <div class="w3-container w3-dark-grey w3-round-xlarge w3-padding" style="width:75%">Photoshop 75%</div>
        </div>
      </div>
    </section>

    <section class='w3-container w3-padding-64' id='portfolio'>
      <h2>Portfolio</h2>
      <p>My projects and work...</p>
    </section>

    <section class='w3-container w3-padding-64' id='contact'>
      <h2>Contact</h2>
      <form @submit.prevent='submitComment'>
        <input v-model='newComment' placeholder='Write a comment...'>
        <button type='submit'>Submit</button>
      </form>
      <ul>
        <li v-for='comment in comments' :key='comment.id'>{{ comment.text }}</li>
      </ul>
    </section>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { createClient } from '@supabase/supabase-js';

const supabase = createClient('https://your-supabase-url', 'your-anon-key');

export default {
  setup() {
    const comments = ref([]);
    const newComment = ref('');

    const fetchComments = async () => {
      let { data } = await supabase.from('comments').select('*');
      comments.value = data;
    };

    const submitComment = async () => {
      await supabase.from('comments').insert([{ text: newComment.value }]);
      newComment.value = '';
      fetchComments();
    };

    onMounted(fetchComments);
    return { comments, newComment, submitComment };
  }
};
</script>

<style>
  /* Add your custom styles here */
  html, body {
    margin: 0;
    padding: 0;
    overflow-x: hidden;
  }
</style>
