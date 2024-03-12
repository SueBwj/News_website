<script setup>
import Header from "./Header.vue";
import Content from "./Content.vue";
</script>

<template>
  <div class="container custom-border-right">
    <Header />
    <Content />
  </div>
</template>
<style>
.custom-border-right {
  border-right: 5px solid rgb(180, 50, 50); /* 自定义右侧边框 */
  box-shadow: 15px 0px 10px -10px rgba(0, 0, 0, 0.51);
}
</style>
