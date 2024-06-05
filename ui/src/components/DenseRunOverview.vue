<template>
  <v-tooltip text="Tooltip">
  Top-10 relevance vectors: {{ judgments }}
  <template v-slot:activator="{ props }">
    <span v-bind="props">
      <canvas ref="canvas" width="200" height="25"/>
    </span>
  </template>
</v-tooltip>
</template>
  
<script lang="ts">
  export default {
    name: "dense-run-overview",
    props: ['judgments'],
    mounted() {
      let canvas = this.$refs.canvas;
      canvas.style = 'border: 1px solid black;'
      canvas = canvas.getContext('2d');

      for (let i in this.judgments) {
        canvas.fillStyle = 'grey'

        if (parseInt(this.judgments[i]) >= 1) {
            canvas.fillStyle = 'green'
        } else if (parseInt(this.judgments[i]) <= 0) {
            canvas.fillStyle = 'red'
        }

        canvas.fillRect(20*i, 0, 100, 100);
        canvas.fillStyle = 'black'
        canvas.fillRect((20*i)-1, 0, 1, 100);
      }
    }
  }
</script>
  