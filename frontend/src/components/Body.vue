<script setup>
import LeftSide from "./LeftSide.vue";
import RightSide from "./RightSide.vue";
</script>

<template>
  <div class="container text-center mt-4">
    <div class="row">
      <div class="col-8">
        <LeftSide />
      </div>
      <div class="col-4">
        <RightSide />
      </div>
    </div>
  </div>
</template>
