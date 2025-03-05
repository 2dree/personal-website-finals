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
    <span class="w3-xxlarge w3-text-white w3-wide">PORTFOLIO</span>
  </div>
</div>


<!-- Container (Portfolio Section) -->
<div class="w3-content w3-container w3-padding-64" id="portfolio">
  <h3 class="w3-center">MY WORK</h3>
  <p class="w3-center"><em>Here are some of my latest lorem work ipsum tipsum.<br> Click on the images to make them bigger</em></p><br>
</div>



<!-- Responsive Grid. Four columns on tablets, laptops and desktops. Will stack on mobile devices/small screens (100% width) -->
<div class="w3-row-padding w3-center">
    <div class="w3-col m3">
      <img src="" style="width:100%" onclick="onClick(this)" class="w3-hover-opacity" alt="The mist over the mountains">
    </div>

    <div class="w3-col m3">
      <img src="" style="width:100%" onclick="onClick(this)" class="w3-hover-opacity" alt="Coffee beans">
    </div>

    <div class="w3-col m3">
      <img src="" style="width:100%" onclick="onClick(this)" class="w3-hover-opacity" alt="Bear closeup">
    </div>

    <div class="w3-col m3">
      <img src="" style="width:100%" onclick="onClick(this)" class="w3-hover-opacity" alt="Quiet ocean">
    </div>
  </div>

  <div class="w3-row-padding w3-center w3-section">
    <div class="w3-col m3">
      <img src="" style="width:100%" onclick="onClick(this)" class="w3-hover-opacity" alt="The mist">
    </div>

    <div class="w3-col m3">
      <img src="" style="width:100%" onclick="onClick(this)" class="w3-hover-opacity" alt="My beloved typewriter">
    </div>

    <div class="w3-col m3">
      <img src="" style="width:100%" onclick="onClick(this)" class="w3-hover-opacity" alt="Empty ghost train">
    </div>

    <div class="w3-col m3">
      <img src="blob:https://www.messenger.com/43e41922-ab32-438d-aff0-0a00bf2759ba" style="width:100%" onclick="onClick(this)" class="w3-hover-opacity" alt="Sailing">
    </div>
    <button class="w3-button w3-padding-large w3-light-grey" style="margin-top:64px">LOAD MORE</button>
  </div>
</div>


<!-- Modal for full size images on click-->
<div id="modal01" class="w3-modal w3-black" onclick="this.style.display='none'">
  <span class="w3-button w3-large w3-black w3-display-topright" title="Close Modal Image"><i class="fa fa-remove"></i></span>
  <div class="w3-modal-content w3-animate-zoom w3-center w3-transparent w3-padding-64">
    <img id="img01" class="w3-image">
    <p id="caption" class="w3-opacity w3-large"></p>
  </div>
</div>
  








    

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