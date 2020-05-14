<template>
  <div>
    <video-bg :sources="[require('../assets/bg-video.mp4')]">
      <slot></slot>
    </video-bg>
  </div>
</template>

<script>
import VideoBg from 'vue-videobg';

export default {
  name: 'BackgroundVideo',
  components: {
    VideoBg
  }
};
</script>
