<script setup>
import { ref, onMounted } from 'vue';
import { supabase } from '../lib/supabase.js';

const comments = ref([]);

const fetchComments = async () => {
  let { data, error } = await supabase.from('comments').select('*');
  if (error) console.error(error);
  else comments.value = data;
};

onMounted(fetchComments);
</script>

<template>
  <div>
    <h2>Guestbook</h2>
    <ul>
      <li v-for="comment in comments" :key="comment.id">
        {{ comment.name }}: {{ comment.message }}
      </li>
    </ul>
  </div>
</template>
