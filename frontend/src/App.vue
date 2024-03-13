<script setup>
import Body from "./components/Body.vue";
import Comments from "./components/Comments.vue";
import Navbar from "./components/Navbar.vue";
import { RouterView } from "vue-router";
</script>

<template>
  <div class="container">
    <div class="row mb-5">
      <Navbar />
    </div>
    <div class="row mt-3">
      <Body />
    </div>
    <div class="row">
      <Comments />
    </div>
  </div>
</template>
