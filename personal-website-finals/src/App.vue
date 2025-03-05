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
      <div class="w3-right w3-hide-small">
        <a href="#about" class="w3-bar-item w3-button w3-hover-opacity">ABOUT</a>
        <a href="#portfolio" class="w3-bar-item w3-button w3-hover-opacity">PORTFOLIO</a>
        <a href="#guestbook" class="w3-bar-item w3-button w3-hover-opacity">GUESTBOOK</a>
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
      <h2>About Me</h2>
      <p>A brief introduction...</p>
      <p>We have created a fictional "personal" website/blog, and our fictional character is a hobby photographer. 
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
    qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    </section>

    <section class='w3-container w3-padding-64' id='portfolio'>
      <h2>Portfolio</h2>
      <p>My projects and work...</p>
    </section>

    <section class='w3-container w3-padding-64' id='guestbook'>
      <h2>Guestbook</h2>
      <form @submit.prevent='submitComment'>
        <input v-model='newComment' placeholder='Write a comment...'>
        <button type='submit'>Submit</button>
      </form>
      <ul>
        <li v-for='comment in comments' :key='comment.id'>{{ comment.text }}</li>
      </ul>
    </section>

    <section class='w3-container w3-padding-64' id='contact'>
      <h2>Contact</h2>
      <p>Get in touch...</p>
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
