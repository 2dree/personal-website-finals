<template>
    <div class="profile">
      <h1>My Profile</h1>
      <!-- Display current profile info if available -->
      <div v-if="profile">
        <p><strong>Name:</strong> {{ profile.name }}</p>
        <p><strong>Bio:</strong> {{ profile.bio }}</p>
      </div>
  
      <!-- Form to update profile -->
      <form @submit.prevent="submitProfile">
        <input v-model="newProfile.name" placeholder="Name" required>
        <textarea v-model="newProfile.bio" placeholder="Bio" required></textarea>
        <button type="submit">Update Profile</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'ProfileComponent',
    data() {
      return {
        profile: null,
        newProfile: {
          name: "",
          bio: ""
        }
      };
    },
    methods: {
      fetchProfile() {
        // Replace with your Flask backend URL
        axios.get('https://your-app.pythonanywhere.com/profile')
          .then(response => {
            // Assume the response is an array of profiles; take the first one
            this.profile = response.data[0] || {};
          })
          .catch(error => {
            console.error("Error fetching profile:", error);
          });
      },
      submitProfile() {
        axios.post('https://your-app.pythonanywhere.com/profile', this.newProfile)
          .then(response => {
            // Refresh profile after update
            this.fetchProfile();
          })
          .catch(error => {
            console.error("Error updating profile:", error);
          });
      }
    },
    mounted() {
      this.fetchProfile();
    }
  };
  </script>
  
  <style scoped>
  .profile {
    max-width: 600px;
    margin: 0 auto;
    padding: 1rem;
  }
  
  /* Responsive design for mobile and tablet */
  @media (max-width: 768px) {
    .profile {
      padding: 0.5rem;
    }
  }
  
  input,
  textarea {
    width: 100%;
    margin: 0.5rem 0;
    padding: 0.5rem;
    box-sizing: border-box;
  }
  
  button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 0.7rem 1.2rem;
    cursor: pointer;
  }
  </style>
  